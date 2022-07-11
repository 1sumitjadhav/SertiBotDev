from rest_framework import serializers 
from coupons.models import Coupons1

 
 
class CouponsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Coupons1
        fields = ('coupons2',
                  'discount')