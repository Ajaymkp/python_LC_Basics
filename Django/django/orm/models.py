from django.db import models


class Author(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.ForeignKey(Author,on_delete=models.CASCADE) 
    date=models.DateField()
    price=models.DecimalField(decimal_places=2,max_digits=5)   

    def __str__(self):
        return self.title