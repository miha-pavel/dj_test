from django.db import models
from django.contrib.auth.models import AbstractUser


class Order(models.Model):
    date = models.DateField(auto_now=True)
    goods = models.CharField(max_length=256)


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now=True)
    order = models.OneToOneField(Order, on_delete = models.CASCADE, null=True, blank=True)