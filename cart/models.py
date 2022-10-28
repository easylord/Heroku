from django.db import models
from authentication.models import User
from product.models import Products

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #books = models.ManyToManyField(Book)
    products = models.ManyToManyField(Products)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'