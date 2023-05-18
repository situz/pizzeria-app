from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    '''Return a string representation of the model'''
    def __str__(self):
        return self.name

class Topping(models.Model):
    '''A topping that belongs to a pizza'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    '''Return a string representation of the model'''
    def __str__(self):
        return self.name[:20]

