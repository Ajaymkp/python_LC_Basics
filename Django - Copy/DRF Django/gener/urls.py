from django.urls import path
from .views import *

urlpatterns = [
    path("add/", Car_add.as_view()),
    path("view/", Car_view.as_view()),
    path("update/<int:pk>/", Car_update.as_view()),
    path("destroy/<int:pk>/", Car_destroy.as_view()),
    path("retupdate/<int:pk>/", Car_ret_update.as_view()),
    path("retdestroy/<int:pk>/", Car_ret_destroy.as_view()),
    path("addview/", Car_add_view.as_view()),
    path("updestroy/<int:pk>/", Car_update_destroy.as_view()),
]