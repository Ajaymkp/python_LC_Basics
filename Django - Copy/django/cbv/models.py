from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.name