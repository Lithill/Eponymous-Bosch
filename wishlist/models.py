from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class ItemWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_item
