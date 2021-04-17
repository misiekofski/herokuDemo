from django.db import models


# Create your models here.

class Bottle(models.Model):
    year_produced = models.DateField()
    storage_date = models.DateField(auto_now_add=True)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=500)