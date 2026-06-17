from rest_framework.serializers import ModelSerializer
from .models import *

class Mobile_Serializer(ModelSerializer):
    class Meta :
        model = Mobile
        fields = "__all__"