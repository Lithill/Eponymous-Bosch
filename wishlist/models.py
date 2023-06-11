from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class UserWishlist(models.Model):

    item_name = models.CharField(max_length=50,)
    item_price = models.IntegerField()
    description = models.TextField()
