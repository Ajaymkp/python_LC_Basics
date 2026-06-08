from django.urls import path
from .views import *
urlpatterns=[
    path("email/",email_sending),
    path("action/",action),
    path("verify/",verification)

]