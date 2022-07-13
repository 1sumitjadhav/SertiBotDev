from django.forms import ModelForm

from coupons.models import Coupons1

# Create the form class.
class CouponForm(ModelForm):
     class Meta:
         model = Coupons1
         fields = '__all__'

# Creating a form to add an article.
# form = CouponForm()

# Creating a form to change an existing article.
# article = Coupons1.objects.get(pk=1)
# form = CouponForm(instance=article)



