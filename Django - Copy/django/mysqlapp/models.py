from django.db import models

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name   


class Order(models.Model):
    product_refer=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    customer_refer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order_id=models.IntegerField(primary_key=True)
    quantity=models.IntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.order_id)
    
