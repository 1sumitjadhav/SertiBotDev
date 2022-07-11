from coupons.viewsets import Couponsviewset
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('',)
router.register('coupons', Couponsviewset, basename='coupon')