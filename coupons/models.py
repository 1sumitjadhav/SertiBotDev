from django.db import models

class Coupons1(models.Model):
    coupons2 = models.CharField(max_length=70, blank=False, default='')
    discount = models.CharField(max_length=200,blank=False, default='')
    # published = models.BooleanField(default=False)