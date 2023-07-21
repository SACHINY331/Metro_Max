from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import product
from .models import category
from .serializers import categoryserialzer
from .serializers import productserialzer

# Create your views here.

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productserialzer

class categoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categoryserialzer    