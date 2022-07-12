from django.db import models

# Create your models here.
class Certificates(models.Model):
    CID = models.BigAutoField(primary_key=True,unique=True)
    fname = models.CharField(max_length=50,blank=False)
    midname = models.CharField(max_length=50,blank=True,null=True)
    lname = models.CharField(max_length=50,blank=True,null=True)
    Phone = models.IntegerField(blank=False)
    Email = models.EmailField(blank=False)
    Course = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.Email
