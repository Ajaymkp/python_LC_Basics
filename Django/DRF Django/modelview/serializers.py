from rest_framework.serializers import ModelSerializer
from .models import *

class car_serializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
    