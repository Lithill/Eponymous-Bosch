from django.db import models
from django.contrib.auth.models import User
from products.models import Product

users = models.ForeignKey(User, on_delete=models.CASCADE)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product,
        through="WishListItem",
        related_name='product_wishlists'
    )
    sale_alert_consent = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'WishList ({self.user})'


class WishListItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their wishlist.
    """

    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
