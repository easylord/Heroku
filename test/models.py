from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from authentication.models import User
import uuid
from subCategory.models import ItemSubCategory
from stores.models import Stores
from product.models import  ProductImageFile
from Reviews.models import Review



class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")



class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.TextField(null=True, blank=False)
    status = models.CharField(default='inactive', max_length=10,null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=20, null=True)
    processor = models.CharField(max_length=20, null=True)
    condition = models.CharField(max_length=20, null=True)
    ram = models.IntegerField(null=True)
    storage_capacity = models.IntegerField(null=True)
    operating_system = models.CharField(max_length=12, null=True)
    color = models.CharField(max_length=12, null=True)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, related_name= "choice_test_item_subcategory", on_delete=models.CASCADE , null=True)
    store_info = models.ForeignKey(Stores , on_delete=models.CASCADE, null=True)

    #start_date = models.DateTimeField(null=True, blank=True)
    #end_date = models.DateTimeField(null=True, blank=True)
    #tags = models.ManyToManyField(Tag)

    #comments = GenericRelation(Comment, related_query_name="question")

    #objects = QuestionManager()


    def __str__(self):
        return self.status

    @property
    def choices(self):
        return self.choice_set.all()


class PhoneItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20,null=True)
    processor = models.CharField(max_length=20,null=True)
    condition = models.CharField(max_length=20,null=True)
    ram= models.IntegerField(null=True)
    storage_capacity = models.IntegerField(null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="phone_created_by")
    operating_system = models.CharField(max_length=12,null=True)
    color = models.CharField(max_length=12,null=True)
    sim = models.CharField(max_length=7,null=True)
    battery= models.IntegerField(null=True)
    camera = models.CharField(max_length=8,null=True)
    item_subcategory = models.ForeignKey(to=ItemSubCategory, on_delete=models.CASCADE , null=True, related_name= "phone_items",)
    store_info = models.ForeignKey(Stores ,related_name= "phone_store_products", on_delete=models.CASCADE, null=True)


   


class Choice(models.Model):
    question = models.ForeignKey('test.Question', on_delete=models.CASCADE, null=True)
    pohone = models.ForeignKey('test.PhoneItems', on_delete=models.CASCADE, null=True) 
    text = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)    
    images = models.ManyToManyField(ProductImageFile, related_name='choicetestimages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True, related_name="choiceowner")
    subCategory = models.ForeignKey("subCategory.subCategory", on_delete=models.CASCADE, null=True, related_name="choicetest_sub")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name="choicetestlikes", blank=True)
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, related_name="choicereviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()

    @property   
    def num_likes(self):
        return self.likes.all().count()



class SecondChoice(models.Model):
    phoneItems=models.ForeignKey("test.PhoneItems", on_delete=models.CASCADE,related_name='phoneItems', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=50, null=True)    
    images = models.ManyToManyField(ProductImageFile, related_name='Second_choicetestimages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE , null=True, related_name="Second_choiceowner")
    subCategory = models.ForeignKey("subCategory.subCategory", on_delete=models.CASCADE, null=True, related_name="Second_choicetest_sub")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    likes = models.ManyToManyField(User, related_name="Second_choicetestlikes", blank=True)
    reviews = models.ManyToManyField(Review, related_name="Second_choicereviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def votes(self):
        return self.answer_set.count()

    @property   
    def num_likes(self):
        return self.likes.all().count()