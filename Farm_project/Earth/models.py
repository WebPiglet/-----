from django.db import models

class DataVegetables(models.Model):
    title = models.CharField(max_length=65)
    price = models.IntegerField(max_length=100)
    description = models.TextField(max_length=1000)
    
