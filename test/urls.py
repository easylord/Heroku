from os import name
from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.LaptopItemsViewsets.as_view(), name='store_home'),
    path('test1/', views.TestItemsViewsets.as_view(), name='store_home'),
    path('product/', views.Products.as_view(), name='product-home'),
    path('phonetest/', views.PhoneViewSet.as_view({"get": "list", "post": "create",'put': 'update',}), name='product-test'),

    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('add/', views.PollViewSet.as_view({"get": "list", "post": "create"}), name='poll_add'),
    path('phone/', views.PhonetestViewSet.as_view({"get": "list", "post": "create"}), name='phone_add'),
    path('phonetest/<id>', views.PhoneDetailView.as_view(), name='phone_add'),
    path('add/<int:id>/', views.PollDetailView.as_view(), name= "details"),
    path('detail/', views.PhoneDetailView.as_view(), name="phonedetail"),
    path('second/', views.create_products, name='file-upload'),
    path('second/<int:id>', views.ProductDetailView.as_view(), name='product_add'),


]