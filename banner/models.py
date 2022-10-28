from django.db import models
import uuid

# Create your models here.

class ProductImage(models.Model):
    media = models.FileField(upload_to='ImageBanner/', null=True)


        
    def media_url(self):
        return self.media.url

class ProductImageFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name= models.CharField(max_length=20, null=True)
    images = models.ManyToManyField(ProductImage, related_name='images', blank=True)

    def __str__(self):
        return f"{self.name}"
        
    
