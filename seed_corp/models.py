from django.db import models

# Create your models here.

class order(models.Model):
    company= models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    state= models.CharField(max_length=20)

class supply(models.Model):
    company=models.ForeignKey(order, on_delete=models.CASCADE)
    kgs= models.IntegerField(default=0)


