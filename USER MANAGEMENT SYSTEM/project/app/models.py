from django.db import models


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)