from django.urls import path
from .views import *
urlpatterns=[
    path("add/",create_data),
    path("view/",view_data),
    path("filter/",filter_data),
    path("asc/",order_by_asc),
    path("slice/",order_by_slice),
    path("desc/",order_by_desc),
    path("del/",delete_data),
    path("select/",select_related),
    path("prefetch/",prefetch_related),
]