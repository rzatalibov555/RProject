from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from services.mixins import DateMixin
from services.uploader import Uploader

from ckeditor.fields import RichTextField

from django.contrib.auth import get_user_model


User = get_user_model()

class Category(MPTTModel, DateMixin):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class Product(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=300)
    description = RichTextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


    def get_new_slug(self, index=0):
        return slugify(self.name) if index == 0 else f"{slugify(self.name)}-{index}"

    def unique_slug_generator(self, index):
        new_slug = self.get_new_slug(index)
        return new_slug if not Product.objects.filter(slug=new_slug).exists() else self.unique_slug_generator(index + 1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug_generator(index=0)
        return super().save(*args, **kwargs)


class ProductImage(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.upload_image_to_product)

    def __str__(self):
        return self.product.name