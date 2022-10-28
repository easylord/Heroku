from django.db import models
import uuid
from django.db import models
from authentication.models import User
from subCategory.models import  ItemSubCategory
from stores.models import Stores
from Reviews.models import Review


class ProductImageFile(models.Model):
    media = models.FileField(upload_to='images/', null=True,)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True, related_name= "finaltest_image")


    def __str__(self):
        return f"{self.owner}'s media images"
        
    def media_url(self):
        return self.media.url


class LapiItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    ram= models.IntegerField()
    storage_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, related_name= "finaltest_item_subcategory", on_delete=models.CASCADE , null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True)

    @property
    def products(self):
        return self.products_set.all()

class MyProducts(models.Model):
    prod_id = models.ForeignKey(LapiItems, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)    
    images = models.ManyToManyField(ProductImageFile, related_name='finaltestimages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True, related_name="finalowner")
    subCategory = models.ForeignKey("subCategory.subCategory", on_delete=models.CASCADE, null=True, related_name="finaltest_sub")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name="finaltestlikes", blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, related_name="finalreviews")


    

    class Meta:

        verbose_name_plural = 'products'
    

    def __str__(self):
        return f"{self.name}"

    @property   
    def num_likes(self):
        return self.likes.all().count()


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)