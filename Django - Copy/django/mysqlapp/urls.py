
from django.urls import path
from .views import *

urlpatterns = [
    path("add/",product_add),
    path("view/",product_view),
    path("update/<int:id>/",product_update,name="update"),
    path("delete/<int:id>/",product_delete,name="delete"),
    path("custadd/",cust_add),
    path("custview/",cust_view),    
    path("custupdate/<int:id>/",cust_update,name="cust_update"),    
    path("custdelete/<int:id>/",cust_delete,name="cust_delete"),
    path("orderadd/",order_add,name="orderadd"),
    path("orderview/",order_view),
    path("orderupdate/<int:id>/",order_update,name="orderup"),
    path("orderdelete/<int:id>/",order_delete,name="orderdel")
]

