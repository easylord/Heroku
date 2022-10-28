from django.urls import path

from .views import create_products

urlpatterns = [
    path('', create_products, name='file-upload'),

]
