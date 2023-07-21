from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import account
from .models import customer
from .serializers import accountserialzer
from .serializers import customerserialzer
from rest_framework.filters import SearchFilter


class accountViewSet(viewsets.ModelViewSet):
    queryset = account.objects.all()
    serializer_class = accountserialzer
    filter_backends=[SearchFilter]
    search_fields=['account_number','account_type']

class customerViewSet(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserialzer    