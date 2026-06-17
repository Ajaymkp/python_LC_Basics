from django.urls import path
from .views import *
urlpatterns = [
    path("empl/", Emp.as_view()),
    path("emp/id/<int:id>/", Emp_id.as_view()),
]