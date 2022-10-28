from itertools import product
from rest_framework import serializers
from .models import Products, ProductImageFile, LaptopProperties
from rest_framework.fields import SerializerMethodField
from authentication.models import User
from stores.serializers import StoreSerializer
from stores.models import Stores
from subCategory.models import subCategory


class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImageFile
        fields = '__all__'
        ref_name= "photo2"


class TweetSerializer(serializers.ModelSerializer):
   # tweep = serializers.SerializerMethodField('get_tweep_username')
    images = ProductImageSerializer(many=True, read_only = True)
    likes= serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many=True)
    subCategory =  serializers.SlugRelatedField(queryset=subCategory.objects.all(), slug_field="name")


    #likes = serializers.SerializerMethodField(read_only=True)
   # images = serializers.ImageField(max_length=None, allow_emp;hty_file=False, allow_null=False, use_url=True, required=False)
    

    class Meta:
        model = Products
        fields = ['id','name', 'description', 'price', 'images' ,'created_at', 'owner','subCategory', 'updated_at', "subCategory", "likes", "num_likes",]
        extra_kwargs = {
            "images": {
                "required": False,
            },'likes': {
                'required' :False,
            }
            
        }

class LaptopPropertiesSerializer(serializers.ModelSerializer):
    product= serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(),)
    store_info = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())

    class Meta:
        model = LaptopProperties
        fields=['brand','model','processor','condition','ram','storage_capacity','operating_system','color','store_info','product']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'product': TweetSerializer(instance.product).data})
        return data

    def create(self, validated_data):
        return LaptopProperties.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     product_data = validated_data.pop('product')
    #     albums = (instance.product).all()
    #     albums = list(albums) 
    #     instance.brand = validated_data.get('brand', instance.brand)
    #     instance.processor = validated_data.get('processor', instance.processor)
    #     instance.condition = validated_data.get('condition', instance.condition)
    #     instance.model = validated_data.get('model', instance.model)
    #     instance.storage_capacity = validated_data.get('storage_capacity', instance.storage_capacity)
    #     instance.operating_system = validated_data.get('operating_system', instance.operating_system)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.store_info = validated_data.get('store_info', instance.store_info)
    #     instance.save()

    #     for products in product_data:
    #         album = albums.pop(0)
    #         album.name = products.get('name', album.name)
    #         album.description = products.get('description', album.description)
    #         album.price = products.get('price', album.price)
    #         #album.images = track_data.get('images', album.images)
    #         album.likes = products.get('likes', album.likes)
    #         #album.reviews = track_data.get('reviews', album.reviews)
    #         album.description = products.get('description', album.description)
    #         album.save()

    #     return instance

    # def update(self, instance, validated_data):
    #     product = validated_data.pop('product', [])
    #     instance = super().update(instance, validated_data)
    #     brand_objs = []
    #     for brand_data in product:
    #         brand = Products.objects.get(**brand_data)
    #         brand_objs.append(brand)
    #         instance.product.set()
    #     return instance



        

    # def get_total_likes(self, instance):
    #     return instance.likes.all().count()

    # def like_count(self,obj):
    #      total_like = self.context.get("likes")
    #      return total_like

    

    
 
 
 
    # function that returns the owner of a tweet
    # def get_tweep_username(self, tweets):
    #     tweep = tweets.tweep.username
    #     return tweep 
