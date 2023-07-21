from django.urls import path,include
from .views import bookViewSet,authorViewSet,reviewViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'book',bookViewSet)
router.register(r'author',authorViewSet)
router.register(r'review',reviewViewSet)


urlpatterns = [
    path('',include(router.urls))

]