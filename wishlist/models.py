from django.db import models
from django.contrib.auth.models import User
from products.models import Product

users = models.ForeignKey(User, on_delete=models.CASCADE)


# Delete the model below eventually and json / everything associated with it
class UserWishlist(models.Model):

    item_name = models.CharField(max_length=50,)
    item_price = models.IntegerField()
    description = models.TextField()


# CURRENT
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product,
        through='WishListItem',
        related_name='product_wishlists'
    )

    def __str__(self):
        return f'Wishlist ({self.user})'


# CURRENT
class WishListSaleItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wishlist} - {self.product}'


# To use if I go with the per item method
class WaitingList(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


# Delete the model below eventually
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
