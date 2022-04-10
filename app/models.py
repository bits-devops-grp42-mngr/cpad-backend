from math import fabs
from operator import truediv
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    emp_number = models.IntegerField(null=False)
    dept = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    image = models.URLField(max_length=200, null=True)

