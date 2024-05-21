import uuid
from django.db.models import TextChoices

class SaveMediaFiles(object):
    def category_img_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/category/{uuid.uuid4()}.{image_extension}"
    
    def product_img_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/product/{uuid.uuid4()}.{image_extension}"
    
    def sponser_img_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"media/sponser/{uuid.uuid4()}.{image_extension}"

class Choises(object):
    class PriceType(TextChoices):
        s = '$', 'USD'
        sum = 'UZS', "so'm"

         


