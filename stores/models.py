from itertools import product
from unicodedata import category
from django.db import models
from authentication.models import User
#from category.models import Category
# Create your models here. 


class Stores(models.Model):
    name = models.CharField(max_length=20)
    description= models.CharField(max_length=200)
    adress = models.CharField(max_length=100)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    delivery = models.BooleanField()
    #product = models.ManyToManyField(Products)


    def __str__(self):
        return str(self.name)