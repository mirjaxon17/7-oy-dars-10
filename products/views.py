from django.shortcuts import render, redirect
from .models import Comment, Category, Sizes, Colors, Product, Choose_Color, Sponser, Favorite, Corzine, Special
from django.contrib.auth.models import User
from django.views import View
from .forms import ProductForm


class HomePageView(View):
    def get(self, request):
        search = request.GET.get('search')
        categorys = Category.objects.order_by('title')[:12]
        products = Product.objects.order_by('-reyting')[:8]
        sponsers = Sponser.objects.all()
        '''userni aniqlash'''
        try:
            username = request.user.username
            user = User.objects.get(username=username)
            '''userni qanda izbraniga sox qigani'''
            user_fav = Favorite.objects.filter(user=user)
            user_fav = len(user_fav)
            '''user qancha narsani savatga saqlagani xaqida malumot'''
            user_corzina = Corzine.objects.filter(user=user)
            user_corzina = len(user_corzina)
                
        except User.DoesNotExist:
            user_corzina = 0
            user_fav = 0
            
            
        pro_two = Category.objects.order_by('-special')[:2]
        new_product = Product.objects.order_by('-create_date')[:8]
        context = {
           'categorys': categorys,
           'products': products,
           'sponsers': sponsers,
           'user_corzina': user_corzina,
            'user_fav' : user_fav,
           'pro_two': pro_two,
           'new_product' : new_product,
        }
        
        return render(request, "index.html", context)
    
    def post(self, request):
        my_fav = request.POST['favorite']
        if my_fav == 'favorite':
            product_name = request.POST['product_name']
            username = request.POST['username']
            product = Product.objects.get(name=product_name)
            user = User.objects.get(username=username)
            favorite = Favorite.objects.create(name=product, user=user)
            favorite.save()
        else:
            product_name = request.POST['product_name']
            username = request.POST['username']
            product = Product.objects.get(name=product_name)
            user = User.objects.get(username=username)
            '''bu postdan request kelayotganini bilish uchun qoshildi!'''
            print(f"_________________{user}_______{product}")
            corzina = Corzine.objects.create(title=product, user=user)
            corzina.save()

        return redirect('home')
    
class ContactListView(View):
    def get (self, request):
        categorys = Category.objects.all()
        username = request.user.username
        user = User.objects.get(username=username)
        '''userni qanda izbraniga sox qigani'''
        user_fav = Favorite.objects.filter(user=user)
        user_fav = len(user_fav)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        user_corzina = Corzine.objects.filter(user=user)
        user_corzina = len(user_corzina)
        context = {
            'categorys':categorys,
            'user_corzina': user_corzina,
            'user_fav' : user_fav,
        }
        return render(request, 'contact.html', context)
    



class UpdateListView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        return render(request, 'add.html', context={'product':product})

    def post(self, request, id):
        new_first_name = request.POST.get('name')
        new_category = request.POST.get('price')

        product = Product.objects.get(id=id)
        product.name = new_first_name
        product.price = new_category
        product.save()
        return redirect("shop")