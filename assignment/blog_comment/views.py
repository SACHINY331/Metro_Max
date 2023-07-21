from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import blog
from .models import comment
from .serializers import blogserialzer
from .serializers import commentserialzer


class blogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = blogserialzer

class commentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = commentserialzer    