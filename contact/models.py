from django.db import models
from django.contrib.auth.models import User


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
    dimensions = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        default='None Chosen')
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
    dominant_colours = models.CharField(
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


# DO NOT USE
class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True)
    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True)
    description = models.TextField()
    dimensions = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    style = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    artist = models.CharField(
        max_length=50,
        null=True,
        blank=True)
    framed = models.BooleanField(
        default=False)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
