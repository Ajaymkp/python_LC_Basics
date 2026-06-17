from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *

# Create your views here.

class Car_add(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer
class Car_view(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer 
class Car_update(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer
class Car_destroy(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer 
class Car_ret_update(RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer
class Car_ret_destroy(RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer

class Car_add_view(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer

class Car_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = Car_Serializer
   