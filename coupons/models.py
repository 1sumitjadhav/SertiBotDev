from django.db import models

class Coupons1(models.Model):
    coupons2 = models.CharField(max_length=100, blank=False, default='')
    discount = models.CharField(max_length=100,blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    
    # published = models.BooleanField(default=False)