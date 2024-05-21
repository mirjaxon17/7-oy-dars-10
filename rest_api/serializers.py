from rest_framework import serializers
from products.models import Comment, Category, Sizes, Colors, Product, Choose_Color, Sponser, Favorite, Corzine, Special


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text','customer']


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = ['id','name']


class CategorySerializer(serializers.ModelSerializer):
    special = SpecialSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id','title','description','special']



class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = ['id','name']

class ColorSeriazlizer(serializers.ModelField):
    class Meta:
        model = Colors
        fields = ['id', 'name']



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    size = SizeSerializer(read_only = True)
    comment = CommentSerializer(read_only =True)
    class Meta:
        model = Product
        fields = ['id','name','description','category','size', 'comment', 'price', 'price_type', 'sale_price', 'reyting', 'how_many']


class ChooseColorSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    class Meta:
        model = Choose_Color
        fields = ['id', 'product', 'color']

class SponserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponser
        fields = ['id', 'name']




    # Ustoz bu pastegi modellar Web App tegishli
    # bolgani uchun Commentga olib qoydim agar bularni xam Api -ga
     # chiqarsak Foydalanuvchilarni danniylari chiqib ketadi deb oyladim

# class FavoriteSerializer(serializers.ModelSerializer):
#     name = ProductSerializer(read_only=True)
#     class Meta:
#         model = Favorite
#         fields = ['id', 'name', 'user']

# class CorzineSerializer(serializers.ModelSerializer):
#     name = ProductSerializer(read_only=True)
#     class Meta:
#         model = Corzine
#         fields = ['id', 'title', 'user']
