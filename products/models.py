from django.db import models
from .helpers import SaveMediaFiles, Choises
from django.contrib.auth.models import User



class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]
    
class Special(models.Model):
    name = models.CharField(max_length=50)
    # image = models.
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True)
    special = models.ForeignKey(Special, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=SaveMediaFiles.category_img_path)
    how_many = models.IntegerField(default=10)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Sizes(models.Model):
    name = models.CharField(max_length=25)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=30)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMediaFiles.product_img_path)
    comment = models.ManyToManyField(Comment)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=Choises.PriceType.choices, default=Choises.PriceType.sum)
    sale_price = models.FloatField(null=True, blank=True)
    reyting = models.FloatField(default=0)
    how_many = models.IntegerField(default=2)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Choose_Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMediaFiles.product_img_path)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)



class Sponser(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.sponser_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name.name


class Corzine(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title.name
        





 
