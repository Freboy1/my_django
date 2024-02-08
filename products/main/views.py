from django.shortcuts import render
from .models import ProductImage

def home(request, image_id=None):
    if image_id is not None:
        try:
            image = ProductImage.objects.get(id=image_id)
        except ProductImage.DoesNotExist:
            return render(request, '404.html')
        context = {'image': image}
        return render(request, 'main/image_details.html', context)
    else:
        return render(request, 'main/home.html')
