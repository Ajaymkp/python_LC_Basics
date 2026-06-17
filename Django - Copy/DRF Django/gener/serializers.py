from rest_framework.serializers import ModelSerializer
from .models import *

class Car_Serializer(ModelSerializer):
    class Meta: 
        model = Car
        fields = "__all__"