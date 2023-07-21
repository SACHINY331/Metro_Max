from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import book
from .models import author
from .models import review
from .serializers import bookserialzer
from .serializers import authorserialzer
from .serializers import reviewserialzer
from rest_framework.filters import SearchFilter


class bookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = bookserialzer
    filter_backends=[SearchFilter]
    search_fields=['author']

    

class authorViewSet(viewsets.ModelViewSet):
    queryset = author.objects.all()
    serializer_class = authorserialzer    

class reviewViewSet(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = reviewserialzer     