from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    class_name = models.CharField(max_length=100)

class university(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    department = models.CharField(max_length=30)
=======

class User(models.Model):
    name = models.CharField(max_length=50,default="None")
    surname = models.CharField(max_length=50,default="None")
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=256,default="None")
>>>>>>> 4cbfd009d838652e1b0161a76f1362a44107cb9d
