from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class ItemWishlist(models.Model):

    item_name = models.CharField(max_length=50, null=True)
    item_price = models.IntegerField(null=True)
    description = models.TextField(null=True)
