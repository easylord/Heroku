from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer

# Create your views here.

class ListCart(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer  