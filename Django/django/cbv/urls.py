from django.urls import path
from .views import *
urlpatterns = [
    path("empadd/", Emp_add.as_view(),name="empadd"),
    path("empview/",Emp_view.as_view()),
    path("empupdate/<int:id>/",Emp_update.as_view(),name="empup"),
    path("empdelete/<int:id>/",Emp_Delete.as_view(),name="empdel")
]