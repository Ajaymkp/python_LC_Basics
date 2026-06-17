from rest_framework.serializers import ModelSerializer
from .models import *

class Stud_serializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"