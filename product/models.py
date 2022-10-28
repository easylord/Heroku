from distutils.command import upload
import uuid
from django.db import models
from authentication.models import User
from Reviews.models import Review
from stores.models import Stores
    
class ProductImageFile(models.Model):
    media = models.FileField(upload_to='images/', null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True)


    def __str__(self):
        return f"{self.owner}'s media images"
        
    def media_url(self):
        return self.media.url


class Products(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)    
    images = models.ManyToManyField(ProductImageFile, related_name='images', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True)
    subCategory = models.ForeignKey("subCategory.subCategory", on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)


    

    class Meta:

        verbose_name_plural = 'Items'
    

    def __str__(self):
        return f"{self.name}"

    @property   
    def num_likes(self):
        return self.likes.all().count()


class LaptopProperties(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    ram= models.IntegerField()
    storage_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    #item_subcategory = models.ForeignKey("subCategory.ItemSubCategory", related_name= "item_subcategories", on_delete=models.CASCADE , null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True, related_name="stores")
    product = models.ForeignKey(Products,related_name= "productproperties", on_delete=models.CASCADE)



class ProductLike(models.Model):
    like = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='all_likes')

    def num_likes(self):
        return self.like.all().count()

    
    
   

  