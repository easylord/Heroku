from rest_framework import serializers
from .models import ProductImageFile, ProductImage



class ProductImageSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductImageFileSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only = True)
  
    class Meta:
        model = ProductImageFile
        fields = '__all__'