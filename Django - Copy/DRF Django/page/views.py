from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from .pagination import *

# Create your views here.

class PageView(ListAPIView):
    queryset = Pagemodel.objects.all()
    serializer_class = Page_serializer
    pagination_class = Defaultpagination