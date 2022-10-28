from django.urls import path

from .views import ListCart, DetailCart

urlpatterns = [
    path('carts', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),
    
]
