from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    phone = PhoneNumberField(blank=True)

class profile(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)

class article(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length= 100 )

    def __str__(self):
        return "%s" % (self.name)

class buy(models.Model):
    article_name = models.ForeignKey(article, on_delete=models.CASCADE,unique=True ,
                                     related_name="user_article")
    def __str__(self):
        return (self.article_name)


class sell(models.Model):
    sell_article = models.OneToOneField(article,unique=True, on_delete=models.CASCADE, blank=False, null=False,
                                     related_name="user_sell")

