from re import L
from .models import *
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from product.serializers import TweetSerializer
from subCategory.models import PhoneItems, LaptopItems, ElectronicsandMobilephonesAcessories


class subCategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = subCategory
        fields = '__all__'


class ItemSubCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = ItemSubCategory  
        fields= "__all__"


class LaptopItemsSerializer(serializers.ModelSerializer):

    product = TweetSerializer(many=True)
    item_subcategory = ItemSubCategorySerializer(read_only=True)
    store_info = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    class Meta:
        model = LaptopItems
        fields= ['id',"brand", 'product','item_subcategory','color','store_info','storage_capacity','ram','condition','processor','model']
        depth = 1
        ref_name= "lapi"

    def create(self, validated_data):
        product_data = validated_data.pop('product',)
        laptop = LaptopItems.objects.create(**validated_data)
        for marks in product_data:
        #laptop.product.add(product_data)
            Products.objects.create(**marks,)
        laptop.save()
        #laptop.marks.set(marks)
        return laptop

class PhoneItemsSerializer(serializers.ModelSerializer):
    product = TweetSerializer(read_only=True,)
    item_subcategory = ItemSubCategorySerializer(read_only=True)

    class Meta:
        model = PhoneItems 
        fields= "__all__"

class FashionItemsSerializer(serializers.ModelSerializer):
    product = TweetSerializer(read_only=True,)
    item_subcategory = ItemSubCategorySerializer(read_only=True)

    class Meta:
        model = FashionItems 
        fields= "__all__"

class ElectronicsSerializer(serializers.ModelSerializer):
    item_subcategory = ItemSubCategorySerializer(read_only=True)

    product = TweetSerializer(read_only=True,)
    class Meta:
        model = ElectronicsandMobilephonesAcessories 
        fields= "__all__"



        


class FinalLinkSerializer(serializers.ModelSerializer):
    product = TweetSerializer(read_only=True,)
    class Meta:
        model = FinalLink 
        fields= "__all__"


