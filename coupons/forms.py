from django.forms import ModelForm

from coupons.models import Coupons1


# Create the form class.
class CouponForm(ModelForm):
     class Meta:
         model = Coupons1
         fields = '__all__'




