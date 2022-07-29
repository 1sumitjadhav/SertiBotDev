from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50,default="None")
    surname = models.CharField(max_length=50,default="None")
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=256,default="None")
