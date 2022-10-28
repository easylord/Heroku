from rest_framework import serializers
from .models import ProductImageFile, LapiItems, MyProducts, Track, Album
from subCategory.models import ItemSubCategory
from stores.models import Stores





class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImageFile
        fields = '__all__'
        ref_name= "photo"


class TheProductSerializer(serializers.ModelSerializer):
   # tweep = serializers.SerializerMethodField('get_tweep_username')
    id = serializers.IntegerField(required=False)
    images = ProductImageSerializer(many=True, read_only = True)

    #likes = serializers.SerializerMethodField(read_only=True)
   # images = serializers.ImageField(max_length=None, allow_emp;hty_file=False, allow_null=False, use_url=True, required=False)
    

    class Meta:
        model = MyProducts
        fields = ['id','name', 'description', 'price', 'images' ,'created_at', 'owner','subCategory', 'updated_at', "subCategory", "likes", "num_likes",]
        extra_kwargs = {
            "images": {
                "required": False,
            },'likes': {
                'required' :False,
            }
            
        }

class ItemSubCategorySerializers(serializers.ModelSerializer):
    class Meta:

        model = ItemSubCategory  
        fields= "__all__"

class LaptopItemsSerializer(serializers.ModelSerializer):

    products = TheProductSerializer(many=True)
    item_subcategory = ItemSubCategorySerializers(read_only=True)
    store_info = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())

    class Meta:
        model = LapiItems
        fields= ['id',"brand", 'products','item_subcategory','color','store_info','storage_capacity','ram','condition','processor','model']
        ref_name= "lapi1"        

    def create(self, validated_data):
        products = validated_data.pop('products')
        #tags = validated_data.pop('tags')
        question = LapiItems.objects.create(**validated_data),
        for product in products:
            MyProducts.objects.create(**product, question=question)
        #question.tags.set(tags)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('products')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if MyProducts.objects.filter(id=choice["id"]).exists():
                    c = MyProducts.objects.get(id=choice["id"])
                    c.text = choice.get('name', c.name)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = MyProducts.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True,)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album