from django.urls import path,include
from .views import accountViewSet,customerViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'account',accountViewSet)
router.register(r'customer',customerViewSet)


urlpatterns = [
    path('',include(router.urls))

]
