from distutils.command import upload
import uuid
from django.db import models
from authentication.models import User
from subCategory.models import subCategory , LaptopItems , ItemSubCategory
from stores.models import Stores
from product.models import Products, ProductImageFile
from Reviews.models import Review

    
class Studentmodel(models.Model):
    stid = models.IntegerField(primary_key=True)
    stname = models.CharField(max_length=100)

class MarksModel(models.Model):
    Marksid = models.IntegerField(primary_key=True)
    maths = models.IntegerField()
    physics = models.IntegerField()
    computer = models.IntegerField()
    stid = models.ForeignKey(Studentmodel, related_name="marks", on_delete=models.CASCADE)


    
   

class TheLaptopItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    ram= models.IntegerField()
    storage_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, related_name= "test_item_subcategory", on_delete=models.CASCADE , null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True)

    @property
    def products(self):
        return self.product_set.all()

class TheProducts(models.Model):
    prod_id = models.ForeignKey(TheLaptopItems, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)    
    images = models.ManyToManyField(ProductImageFile, related_name='testimages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True, related_name="owner")
    subCategory = models.ForeignKey("subCategory.subCategory", on_delete=models.CASCADE, null=True, related_name="test_sub")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name="testlikes", blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, related_name="reviews")


    

    class Meta:

        verbose_name_plural = 'products'
    

    def __str__(self):
        return f"{self.name}"

    @property   
    def num_likes(self):
        return self.likes.all().count()

