from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    PhoneItems,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
    Question,
    Choice,
    PhoneItems,
    SecondChoice
    
)

# admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(PhoneItems)
admin.site.register(SecondChoice)



class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


#@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


#@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]

#@admin.register(ProductSpecification)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        
    ]