from django.db import models
from django.forms import CharField
from pyparsing import Char

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
    
