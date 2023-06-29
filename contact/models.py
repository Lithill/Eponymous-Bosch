from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Commission(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=100)
    email = models.EmailField(
        max_length=100)
    description = models.TextField()
    width_in_mm = models.IntegerField(
        null=True,
        blank=True,
        default=None,
        validators=[MaxValueValidator(1189)]
    )
    height_in_mm = models.IntegerField(
        null=True,
        blank=True,
        default=None,
        validators=[MaxValueValidator(1189)]
    )
    style = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default='None Chosen')
    artist = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default='None Chosen')
    framed = models.BooleanField(
        default=False)
    medium = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default='None Chosen')
    status = models.TextField(
        null=True,
        blank=True,
        default='We are looking at your request and will update you soon!')
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
