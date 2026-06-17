from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    stock=models.IntegerField()
    
    def __str__(self):
        return self.name

class Order_items(models.Model):
    product=models.ForeignKey(Items,on_delete=models.CASCADE)
    order_id=models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return str(self.order_id)