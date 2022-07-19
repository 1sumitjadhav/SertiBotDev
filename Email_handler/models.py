from django.db import models

# Create your models here.
class Certificates(models.Model):
    temp_id = models.CharField(default="0",max_length=10,blank=False)
    cert_id = models.CharField(default="None",max_length=16,blank=False)
    fname = models.CharField(max_length=50,blank=False)
    midname = models.CharField(max_length=50,blank=True,null=True)
    lname = models.CharField(max_length=50,blank=True,null=True)
    Phone = models.IntegerField(blank=False)
    Email = models.EmailField(blank=False)
    Course = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.cert_id
