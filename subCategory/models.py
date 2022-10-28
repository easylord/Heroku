from tkinter import CASCADE
from django.db import models
from category.models import Category
from product.models import Products
from stores.models import Stores

# Create your models here.

class subCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='subCategoryimages/',blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE , null=True)


    def __str__(self):
        return self.name

class ItemSubCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name




class LaptopItems(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    ram= models.IntegerField()
    storage_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, related_name= "item_subcategory", on_delete=models.CASCADE , null=True)
    product = models.ManyToManyField(Products,related_name= "product")
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True, related_name="store")


class PhoneItems(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    ram= models.IntegerField()
    storage_capacity = models.IntegerField()
    operating_system = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    sim = models.CharField(max_length=7)
    battery= models.IntegerField()
    camera = models.CharField(max_length=8)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "phoneproducts", on_delete=models.CASCADE, null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True)
  


class FashionItems(models.Model):
    brand = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    type= models.CharField(max_length=20)
    size= models.TextField(max_length=10)
    sleeve_lenght = models.CharField(max_length=10)
    color = models.CharField(max_length=12)
    condition = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "fashionproducts", on_delete=models.CASCADE, null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True)





class FoodandDrinks(models.Model):
    type = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "foodproducts", on_delete=models.CASCADE, null=True)



class HealthandBeauty(models.Model):
    brand = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "healthproducts", on_delete=models.CASCADE, null=True)



class FurnitureandAppliacnes(models.Model):
    type = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "furnituresproducts", on_delete=models.CASCADE, null=True)




class JobsandSkills(models.Model):
    type = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    years_of_experience = models.IntegerField()
    requirements = models.TextField(max_length=20)
    responsibilities = models.TextField(max_length=20)
    qualification = models.TextField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "jobproducts", on_delete=models.CASCADE, null=True)



class CarsandAutomobile(models.Model):
    type = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year= models.IntegerField()
    milleage= models.IntegerField()
    transmission = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "carsproducts", on_delete=models.CASCADE, null=True)



class HousesandProperties(models.Model):
    adress = models.CharField(max_length=100)
    type_of_property = models.CharField(max_length=20)
    furnished = models.CharField(max_length=20)
    parking_spaces = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "houseproducts", on_delete=models.CASCADE, null=True)




class HousingandHotelRent(models.Model):
    bathroom = models.CharField(max_length=100)
    bedroom = models.CharField(max_length=20)
    furnished = models.CharField(max_length=20)
    parking_spaces = models.CharField(max_length=20)
    pets = models.CharField(max_length=20)
    service_charge = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "housingproducts", on_delete=models.CASCADE, null=True)



class ElectronicsandMobilephonesAcessories(models.Model):
    type = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    condition = models.CharField(max_length=20)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True)
    product = models.ForeignKey(Products,related_name= "electronicsproducts", on_delete=models.CASCADE, null=True)



class FinalLink(models.Model):
    laptop_items= models.ForeignKey(LaptopItems, on_delete=models.CASCADE, null=True)
    phone_items = models.ForeignKey(PhoneItems, on_delete=models.CASCADE, null=True)


    










    
    
