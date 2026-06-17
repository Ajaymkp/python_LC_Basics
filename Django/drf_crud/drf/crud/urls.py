from django.urls import path
from .views import *

urlpatterns = [
    path("view/", Emp_view.as_view()),
    path("add/<int:id>/", Emp_id.as_view())
]