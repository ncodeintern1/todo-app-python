from django.db import models

# Create your models here.
class user(models.Model):
    Name= models.CharField(max_length=20)
    coutry =models.CharField(max_length=15)
    Password = models.CharField(max_length=20)
