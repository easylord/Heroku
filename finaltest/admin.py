from django.contrib import admin
from .models import LapiItems,  MyProducts, Track, Album

# Register your models here.
admin.site.register(MyProducts)
admin.site.register(LapiItems)
admin.site.register(Track)
admin.site.register(Album)