
from django.forms import ModelForm
from .models import *


class Product_form(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        
class Customer_form(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"   

class Order_form(ModelForm):
    class Meta:
        model=Order
        fields=["product_refer","customer_refer","order_id","quantity"]