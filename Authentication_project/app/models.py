from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact = models.IntegerField()
    email = models.EmailField()