from django.db import models
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=100)

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def image_tag(self):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % (self.image.url))

    image_tag.short_description = 'Image'
