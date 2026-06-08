from .models import *
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

@receiver(post_save,sender=Order_items)

def reduce_stock(sender,instance,created,**kwargs):
    if created:
        product=instance.product
        product.stock=product.stock - instance.quantity
        product.save()
        print(f" stock reduced for {product.name} by {product.stock}")

@receiver(post_delete,sender=Order_items)
def return_stock(sender,instance,**kwargs):
    product=instance.product
    product.stock=product.stock + instance.quantity
    product.save()
    print(f" stock product {product.name} by {product.stock}")