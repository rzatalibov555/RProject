from django.contrib import admin

from .models import Category, Product, ProductImage

admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(ProductImage)

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    inlines = (ProductImageAdmin, )

admin.site.register(Product, ProductAdmin)