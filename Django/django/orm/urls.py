from django.urls import path
from .views import *
urlpatterns=[
    path("add/",create_data),
    path("view/",view_data),
]