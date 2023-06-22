from django.db import models


class Commission(models.Model):
    name = models.CharField(
        max_length=100)
    email = models.EmailField(
        max_length=100)
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
