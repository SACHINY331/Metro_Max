from django.urls import path,include
from .views import productViewSet,categoryViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'product',productViewSet)
router.register(r'category',categoryViewSet)


urlpatterns = [
    path('',include(router.urls))

]
