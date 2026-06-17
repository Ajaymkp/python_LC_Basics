from rest_framework.serializers import ModelSerializer
from .models import *

class Page_serializer(ModelSerializer):
    class Meta :
        model = Pagemodel
        fields = "__all__"