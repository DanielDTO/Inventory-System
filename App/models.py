from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.



class Inventory(models.Model): #name of table

    Date = models.DateTimeField(default=datetime.now, blank= False)
    Name = models.CharField(max_length=100, blank= False)  #Name of column
    Price = models.IntegerField()
    Category = models.CharField(max_length=100, blank= False)
    Quantity = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])
    # To avoid choosing irrelevant options
    choices = (
        ('AVAILABLE', 'Item ready'),
        ('RESTOCKING', 'Item will be ready in a few days'),
        ('SOLD', 'Item Sold')
    )

    Status = models.CharField(max_length=10, choices= choices, default="SOLD")   #Sold/Available/Restocking

#Make Inventory abstract to avoid creating Inventory table
    class Meta:
        abstract = True

    def __str__(self):
        return 'Name: {0} Price: {1} Category: {2}'.format(self.Name, self.Price, self.Category)

# classes that inherit 'Inventory' class

class Laptop(Inventory):
    pass

class Desktop(Inventory):
    pass

class Mobile(Inventory):
    pass

class Stationary(Inventory):
    pass


