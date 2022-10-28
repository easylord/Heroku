from asyncore import read
from cgitb import lookup, text
from dataclasses import fields
from rest_framework import serializers
from .models import Category, Product, ProductSpecificationValue ,ProductType , Choice , Question, PhoneItems, SecondChoice
from rest_framework_recursive.fields import RecursiveField
from product.serializers import ProductImageSerializer
from Reviews.serializers import ReviewSerializer
from product.models import ProductImageFile
from Reviews.models import Review
from subCategory.models import subCategory
from authentication.models import User


class TreeNodeSerializer(serializers.ModelSerializer):
    leaf_nodes = serializers.SerializerMethodField()

    class Meta:
        depth = 1
        model = Category
        fields = ("node_name", "image", "mineraltypes", "leaf_nodes")

    def get_leaf_nodes(self, obj):
        return TreeNodeSerializer(obj.get_children(), many=True).data

class CategorySerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']

class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ['id', 'name',]


class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    specification = ProductTypeSerializer()
    class Meta:
        model = ProductSpecificationValue
        fields = ['id', 'product', 'specification','value']


class ProductSerializer(serializers.ModelSerializer):
    specification = ProductSpecificationValue()
    product_type = ProductTypeSerializer()
    class Meta:
        model = Product
        fields = ['id', 'product_type', 'title', 'description', 'regular_price','discount_price', 'specification']
    

class ChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Choice
        fields = [
            'id',
            'question',
            "pohone",
            'text',
            'name',
            'description',
            'price',
            'images',
            'created_at',
            'owner',
            'subCategory',
            'updated_at',
            'likes',
            'reviews'



        ]
        read_only_fields = ('question',)
        extra_kwargs = {
            "images": {
                "required": False,
            },'likes': {
                'required' :False,
            }, "pohone": {
                "required" : False
            }, "question": {
                "required" : False
            }
            
        }

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    #tags = TagSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "brand",
            "status",
            "created_by",
            "choices",
            "model",
            "processor",
            "condition",
            "ram",
            "storage_capacity",
            "operating_system",
            "color",
            "item_subcategory",
            "store_info"
            
        ]
        #read_only_fields = ["tags"]

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        #tags = validated_data.pop('tags')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(**choice, question=question)
        #question.tags.set(tags)
        return question

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id=choice["id"])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance




   #def create(self, validated_data):
        """
        Serializes an image if it has been uploaded, then passes the image
        back to the validated_data to finish creating the Announcement.
        """
        # review_data = validated_data.pop("reviews")

        # reviews =[]
        # for review in review_data :
        #     review_obj = Review.objects.create(**review)
        #     reviews.append(review_obj)

        # phone_items = SecondChoice.objects.create(**validated_data)
        # phone_items.reviews.set(reviews)

        # image_data = self.context['request'].FILES
        # if image_data:
        #     serializer = ProductImageSerializer(data=image_data)
        #     serializer.is_valid(raise_exception=True)
        #     image = serializer.save()
        #     validated_data['images'] = image
        # return super().create(validated_data)

        # def create(self, validated_data):
        #  image_data = validated_data.pop('images')
        #  secondchoice = SecondChoice.objects.create(**validated_data)
        #  for image_data in image_data:
        #      ProductImageFile.objects.create(**image_data)

        #  return secondchoice


    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('likes')
    #     reviews = validated_data.pop('reviews')
    #     phoneItems = PhoneItems.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         SecondChoice.objects.create(phoneItems=phoneItems, **track_data)
    #     phoneItems.likes.set(reviews)
    #     return phoneItems
    # def create(self, validated_data):
    #     question = validated_data.pop('sub_cat')
    #     #tags = validated_data.pop('tags')
    #     details = PhoneItems.objects.create(**validated_data)
    #     for detail in details_data:
    #         Choice.objects.create(**detail)
    #     #question.tags.set(tags)
    #     return details

class SecondChoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    images = ProductImageSerializer(many =True, required= False)
    reviews = ReviewSerializer(many=True,required= False)
    subCategory =  serializers.SlugRelatedField(queryset=subCategory.objects.all(), slug_field="name")
    likes= serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), many=True)

    class Meta:
        model = SecondChoice
        fields = [
            'id',
            'text',
            'name',
            'description',
            'price',
            'images',
            'created_at',
            'owner',
            'subCategory',
            'updated_at',
            'likes',
            'reviews'
        ]

        extra_kwargs = {
            'reviews': {
                'required' :False
            },'images': {
                'required' :False
            }, 'likes': {
                'required': False
            }
            

        }


    def create (self, validated_data):
        images = validated_data.pop("images")
        review_data = validated_data.pop("reviews")
        liked_data = validated_data.pop("likes")


        image_data= []
        for image in images:
            img_obj= ProductImageFile.objects.create(**image)
            image_data.append(img_obj)

        reviews =[]
        for review in review_data :
            review_obj = Review.objects.create(**review)
            reviews.append(review_obj)

        likes =[]
        for like in liked_data :
            like_obj = SecondChoice.objects.create(**like)
            likes.append(like_obj)

        phone_items = SecondChoice.objects.create(**validated_data)
        phone_items.images.set(images)
        phone_items.reviews.set(reviews)
        phone_items.likes.set(likes)
        return phone_items

    def update(self, instance, validated_data):
        track_data = validated_data.pop('images')
        albums = (instance.images).all()
        albums = list(albums) 
        instance.text = validated_data.get('text', instance.text)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.images = validated_data.get('images', instance.images)
        instance.likes = validated_data.get('likes', instance.like)
        instance.reviews = validated_data.get('reviews', instance.reviews)
        instance.save()

        for track_data in track_data:
            album = albums.pop(0)
            album.media = track_data.get('media', album.text)
            album.save()

        return instance
                # image_data = validated_data.pop('images')
                # review_data = validated_data.pop('reviews')
                # instance = super().update(instance, validated_data)

                # image_obj=[]
                # review_obj=[]
                # for image_data in image_data:
                #     image = ProductImageFile.objects.get(**image_data)
                #     image_obj.append(image)
                #     instance.images.set(image_obj)
                # for review_data in review_data:
                #     review = Review.objects.get(**review_data)
                #     review_obj.append(review)
                #     instance.reviews.set(review_obj)
                # return instance
           

 



    # def create(self, validated_data):
    #     image_data = validated_data.pop('images')
    #     products = []
    #     for phone in image_data:
    #         images = phone.pop("images")
    #         phone_obj =ProductImageFile.objects.create(**phone)
    #         phone_obj.images.set(images)
    #         products.append(phone_obj)
    #     product = SecondChoice.objects.create(**validated_data)
    #     product.images.set(products)
    #     return product

    



class PhoneItemsSerializer(serializers.ModelSerializer):
    phoneItems = SecondChoiceSerializer(many=True)
    class Meta:
        model = PhoneItems
        fields = [
            "id",
            "brand",
            "processor",
            "created_by",
            "phoneItems",
            "model",
            "processor",
            "condition",
            "ram",
            "sim",
            "camera",
            "storage_capacity",
            "operating_system",
            "color",
            "item_subcategory",
            "store_info",
            "battery"            
        ]
        lookup_field = "id"
       # read_only_fields = ["details"]


    def create(self, validated_data):
        phone_items_data = validated_data.pop('phoneItems')
        products = []
        for phone in phone_items_data:
            likes = phone.pop("likes")
           # reviews = phone.pop("reviews")
            phone_obj =SecondChoice.objects.create(**phone,)
            phone_obj.likes.set(likes)
           # phone_obj.reviews.set(reviews)
            products.append(phone_obj)


        
        product = PhoneItems.objects.create(**validated_data)
        product.phoneItems.set(products)
        return product

        

    def update(self, instance, validated_data):
        track_data = validated_data.pop('phoneItems')
        albums = (instance.phoneItems).all()
        albums = list(albums) 
        instance.brand = validated_data.get('brand', instance.brand)
        instance.processor = validated_data.get('processor', instance.processor)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.model = validated_data.get('model', instance.model)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.sim = validated_data.get('sim', instance.sim)
        instance.camera = validated_data.get('camera', instance.camera)
        instance.storage_capacity = validated_data.get('storage_capacity', instance.storage_capacity)
        instance.operating_system = validated_data.get('operating_system', instance.operating_system)
        instance.color = validated_data.get('color', instance.color)
        instance.battery = validated_data.get('battery', instance.battery)
        instance.save()

        for track_data in track_data:
            album = albums.pop(0)
            album.text = track_data.get('text', album.text)
            album.name = track_data.get('name', album.name)
            album.description = track_data.get('description', album.description)
            album.price = track_data.get('price', album.price)
            #album.images = track_data.get('images', album.images)
            #album.likes = track_data.get('likes', album.likes)
            #album.reviews = track_data.get('reviews', album.reviews)
            album.description = track_data.get('description', album.description)
            album.save()

        for images in track_data:
            album = albums.pop(1)
            album.media = images.get('media', album.media)
            album.save()

        # for image_data in track_data:
        #     image = album.pop(0)
        #     image.name = image_data.get('name',image.name)
        #     image.save()

        return instance

    # def create(self, validated_data):
    #     details_data = validated_data.pop('sub_cat')
    #     #tags = validated_data.pop('tags')
    #     details = PhoneItems.objects.create(**validated_data)
    #     for detail in details_data:
    #         Choice.objects.create(**detail)
    #     #question.tags.set(tags)
    #     return details
    
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['details'] = SecondChoiceSerializer(instance.details).data
    #     return rep

    # def update(self, instance, validated_data):
    #     tracks_data = validated_data.pop('phoneItems')
    #     instance.brand = validated_data.get("brand", instance.brand)
    #     instance.save()
    #     keep_choices = []
    #     for choice in tracks_data:
    #         if "id" in choice.keys():
    #             if SecondChoice.objects.filter(id=choice["id"]).exists():
    #                 c = SecondChoice.objects.get(id=choice["id"])
    #                 c.text = choice.get('text', c.text)
    #                 c.save()
    #                 keep_choices.append(c.id)
    #             else:
    #                 continue
    #         else:
    #             c = SecondChoice.objects.create(**choice,)
    #             keep_choices.append(c.id)

    #     for choice in instance.phoneItems:
    #         if choice.id not in keep_choices:
    #             choice.delete()

    #     return instance

    