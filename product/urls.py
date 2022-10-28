from django.urls import path

from .views import create_products, product_detail, LaptopViewSet, LaptopDetailView, topic_content_list

urlpatterns = [
    path('', create_products, name='file-upload'),
    path('lapitest', topic_content_list, name='file-test'),
    path('lapi/<id>/',product_detail,name = 'employee-detail'),
    path('laptop/', LaptopViewSet.as_view({"get": "list", "post": "create",'put': 'update',}), name='product-test'),
    path('laptop/<id>', LaptopDetailView.as_view(), name='laptop-test'), 
]
