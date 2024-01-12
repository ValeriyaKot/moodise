from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Picture(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Board(models.Model):
    name = models.CharField(max_length=250)
    images = models.ManyToManyField(Picture, blank=True, null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="boards")