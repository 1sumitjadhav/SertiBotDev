from django.db import models

class Coupons1(models.Model):
    coupons2 = models.CharField(max_length=100, blank=False, default='')
    discount = models.IntegerField(blank=False, default='')
    valid_for = models.IntegerField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coupons2
    # published = models.BooleanField(default=False)