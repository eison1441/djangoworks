from django.db import models

# Create your models here.

class Book(models.Model):

    title=models.CharField(max_length=200)

    auther=models.CharField(max_length=200)

    price=models.PositiveIntegerField()

    genre=models.CharField(max_length=100)

    language=models.CharField(max_length=100)

    year=models.CharField(max_length=10)

    













