from django.urls import path
from .views import *
urlpatterns=[
    path("func/",func),
    path("html/",html),
    path("home/",home),
    path("about/",about),
    path("service/",service),
    path("contact/",contact),
    path("studadd/",student,name="add"),
    path("view/",view),
    path("update/<int:id>/",student_update,name="update"),
    path("delete/<int:id>/",student_delete,name="delete"),
]
