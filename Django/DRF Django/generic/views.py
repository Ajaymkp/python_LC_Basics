from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *

# Create your views here.

'''
CreateAPIView              # add
ListAPIView                # view

ListCreateAPIView            #  add and view

RetrieveAPIView              # get element by id
UpdateAPIView                # update
DestroyAPIView               # delete

RetrieveUpdateAPIView         # get element by id and delete
RetrieveDestroyAPIView

RetrieveUpdateDestroyAPIView  # get element by id and update or delete 
'''

class Mobile_add_view(ListCreateAPIView):
    queryset=Mobile.objects.all()
    serializer_class=Mobile_Serializer

class Mobile_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = Mobile_Serializer

