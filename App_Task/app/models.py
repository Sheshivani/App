from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(unique=True)
    # test = models.BigIntegerField()
    # name = models.CharField(max_length = 55)
    # phone = models.BigIntegerField(max_length=25, blank=True, null=True)


class Spam(models.Model):
    phone = PhoneNumberField()
    by = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
