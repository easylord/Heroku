from venv import create
from rest_framework import serializers
from .models import MarksModel , Studentmodel, ProductImageFile, Products , LaptopItems, TheLaptopItems, TheProducts
from subCategory.models import ItemSubCategory
from stores.models import Stores


class Marksserializer(serializers.ModelSerializer):
    #images = serializers.SerializerMethodField()
    #images = ProductImageSerializer(many=True)

    class Meta:
        model = MarksModel
        fields = "__all__"
        

class Studentserializer(serializers.ModelSerializer):
    #images = serializers.SerializerMethodField()
    #images = ProductImageSerializer(many=True)
    marks = Marksserializer(many=True)
    class Meta:
        model = Studentmodel
        fields = "__all__"

    def create(self, validated_data):
        marks = validated_data.pop('marks')
        laptop = Studentmodel.objects.create(**validated_data)
        for choice in marks:
        #laptop.product.add(product_data)
            MarksModel.objects.create(**choice)
        #laptop.marks.set(marks)
        return laptop

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImageFile
        fields = '__all__'


class TheProductSerializer(serializers.ModelSerializer):
   # tweep = serializers.SerializerMethodField('get_tweep_username')
    id = serializers.IntegerField(required=False)
    images = ProductImageSerializer(many=True, read_only = True)

    #likes = serializers.SerializerMethodField(read_only=True)
   # images = serializers.ImageField(max_length=None, allow_emp;hty_file=False, allow_null=False, use_url=True, required=False)
    

    class Meta:
        model = TheProducts
        fields = ['id','name', 'description', 'price', 'images' ,'created_at', 'owner','subCategory', 'updated_at', "subCategory", "likes", "num_likes",]
        extra_kwargs = {
            "images": {
                "required": False,
            },'likes': {
                'required' :False,
            }
            
        }

class ItemSubCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = ItemSubCategory  
        fields= "__all__"

class LaptopItemsSerializer(serializers.ModelSerializer):

    products = TheProductSerializer(many=True)
    item_subcategory = ItemSubCategorySerializer(read_only=True)
    store_info = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    class Meta:
        model = TheLaptopItems
        fields= ['id',"brand", 'products','item_subcategory','color','store_info','storage_capacity','ram','condition','processor','model']
        

    def create(self, validated_data):
        products = validated_data.pop('products')
        #tags = validated_data.pop('tags')
        question = TheLaptopItems.objects.create(**validated_data)
        for product in products:
            TheProducts.objects.create(**product, question=question)
        #question.tags.set(tags)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('products')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if TheProducts.objects.filter(id=choice["id"]).exists():
                    c = TheProducts.objects.get(id=choice["id"])
                    c.text = choice.get('name', c.name)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = TheProducts.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance
