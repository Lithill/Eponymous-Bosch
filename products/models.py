from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=1,
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
        related_name="user_wishlist",
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
    on_sale = models.BooleanField()
    discount = models.IntegerField(
        validators=[
            MaxValueValidator(95),
            MinValueValidator(0)
        ]
    )
    discounted_price = models.IntegerField(
        null=True,
    )
    sell_price = models.IntegerField(null=True)

    @property
    def discounted_price(self):
        return round(((self.og_price) * (self.discount)) / 100, 2)

    @property
    def sell_price(self):
        return (self.og_price)-(self.discounted_price)

    @property
    def on_sale(self):
        return (self.discount > 0)
