from django.urls import path
from .views import *

urlpatterns = [
    path("mob/",Mobile_add_view.as_view()),
    path("mob/<int:pk>/",Mobile_update_destroy.as_view()),
]

