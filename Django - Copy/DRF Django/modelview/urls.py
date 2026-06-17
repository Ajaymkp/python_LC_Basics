from django.urls import path,include
from .routers import *

urlpatterns = [
    path("car/", include(carroute.urls))
]