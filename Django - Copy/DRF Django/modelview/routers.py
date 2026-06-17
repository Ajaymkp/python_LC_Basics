from rest_framework.routers import DefaultRouter
from .views import *

carroute=DefaultRouter()
carroute.register(r"route", CarView)
