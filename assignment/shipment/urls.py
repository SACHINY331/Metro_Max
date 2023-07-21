from django.urls import path,include
from .views import shipmentViewSet,cargoViewSet,trackingViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'shipment',shipmentViewSet)
router.register(r'cargo',cargoViewSet)
router.register(r'tracking',trackingViewSet)


urlpatterns = [
    path('',include(router.urls))

]