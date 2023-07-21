from django.urls import path,include
from .views import blogViewSet,commentViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'blog',blogViewSet)
router.register(r'comment',commentViewSet)


urlpatterns = [
    path('',include(router.urls))

]
