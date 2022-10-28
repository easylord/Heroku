from django.urls import  path

from .views import CategoryViewSet

urlpatterns = [
    path('', CategoryViewSet, name='file-upload'),

]
