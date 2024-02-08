from django.contrib import admin
from .models import Product, ProductImage

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image_tag')

admin.site.register(Product)
admin.site.register(ProductImage, ProductImageAdmin)
