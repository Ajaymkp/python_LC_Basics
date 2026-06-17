from django.urls import path
from .views import *

urlpatterns = [
    path("add/", add_data),
    path("view/", view_data),
    path("view/id/<int:id>/",view_id),
    path("patch/id/<int:id>/",patch_data),
    path("delete/id/<int:id>/",delete_data),
]

