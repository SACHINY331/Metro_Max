from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import shipment
from .models import cargo
from .models import tracking
from .serializers import shipmentserialzer
from .serializers import cargoserialzer
from .serializers import trackingserialzer


class shipmentViewSet(viewsets.ModelViewSet):
    queryset = shipment.objects.all()
    serializer_class = shipmentserialzer

    

class cargoViewSet(viewsets.ModelViewSet):
    queryset = cargo.objects.all()
    serializer_class = cargoserialzer    

class trackingViewSet(viewsets.ModelViewSet):
    queryset = tracking.objects.all()
    serializer_class = trackingserialzer     