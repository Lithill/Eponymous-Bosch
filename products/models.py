from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from wishlist.email import send_sale_alert_email


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    name = models.CharField(
        max_length=254
    )
    description = models.TextField()
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    original_artist = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    users_wishlist = models.ManyToManyField(
        User,
        related_name="users_wishlist",
        blank=True)
    style = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    orientation = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    imperial = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    metric = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    year = models.IntegerField()
    orig_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    og_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    on_sale = models.BooleanField(
        default=False
    )
    on_sale_start = models.DateField(
        null=True,
        blank=True
    )
    on_sale_end = models.DateField(
        null=True,
        blank=True
    )
    discount_percentage = models.IntegerField(
        validators=[
            MaxValueValidator(95),
            MinValueValidator(0)
        ]
    )
    discounted_price = models.IntegerField(
        null=True,
    )
    sell_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    @property
    def discounted_price(self):
        return round(((self.og_price) * (self.discount_percentage)) / 100, 2)

    @property
    def on_sale(self):
        return (self.discount_percentage > 0)

    def clean(self):
        discount_condition = (
            self.discount_percentage is None or self.discount_percentage > 0
        )

        # Stop admin entering dates without giving a discount
        if (
            self.on_sale_start
            and self.on_sale_end
            and discount_condition
        ):
            raise ValidationError("Please enter the discount percentage.")

        # Stop user making the end date earlier than the sale start date
        if self.on_sale_start and self.on_sale_end:
            if self.on_sale_end < self.on_sale_start:
                raise ValidationError(
                    "The sale end date cannot be before the sale start date.")

    def save(self, *args, **kwargs):
        self.sell_price = self.og_price - self.discounted_price

        # If user does not add a sale date when adding discount
        # todays date is auto added
        if self.on_sale and not self.on_sale_start:
            self.on_sale_start = timezone.now().date()

        # If user does not add an end date
        # a week is auto added
        if self.on_sale_start and not self.on_sale_end:
            self.on_sale_end = self.on_sale_start + timedelta(days=7)

        # If user tries to end the sale early by only changing discount to 0
        # automatically set the dates to none
        if self.discount_percentage == 0:
            self.on_sale_start = None
            self.on_sale_end = None

        # When sale ends, automatically turn off sale and discount
        if self.on_sale_end and self.on_sale_end < timezone.now().date():
            self.discount_percentage = 0
            self.on_sale_start = None
            self.on_sale_end = None

        super().save(*args, **kwargs)

        if self.on_sale:
            # Create array of users
            users_with_product = self.product_wishlists.filter(
                sale_alert_consent=True).values_list('user', flat=True)

            for user_id in users_with_product:
                user = User.objects.get(id=user_id)
                send_sale_alert_email(user, self)
