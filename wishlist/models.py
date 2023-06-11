from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Delete the model below eventually and json / everything associated with it
class UserWishlist(models.Model):

    item_name = models.CharField(max_length=50,)
    item_price = models.IntegerField()
    description = models.TextField()


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item
