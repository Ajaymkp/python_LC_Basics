from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.

class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = car_serializer