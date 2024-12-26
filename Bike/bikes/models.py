from django.db import models

# Create your models here.

class Bike(models.Model):
    
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    price=models.PositiveBigIntegerField()
    fuel_type=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    mileage=models.PositiveIntegerField()

