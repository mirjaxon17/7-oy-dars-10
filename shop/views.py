from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from products.models import Comment, Category, Sizes, Colors, Product, Choose_Color, Sponser, Favorite, Corzine, Special
from django.contrib.auth.mixins import LoginRequiredMixin



class ShopListView(LoginRequiredMixin, View):
    def get(self, request):
        categorys = Category.objects.order_by('title')[:12]
        products = Product.objects.all()
        sponsers = Sponser.objects.all()
        '''userni aniqlash'''
        username = request.user.username
        user = User.objects.get(username=username)
        '''userni qanda izbraniga sox qigani'''
        user_fav = Favorite.objects.filter(user=user)
        user_fav = len(user_fav)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        user_corzina = Corzine.objects.filter(user=user)
        user_corzina = len(user_corzina)

        sizes = Sizes.objects.all()
        colors = Colors.objects.all()
        pro_two = Category.objects.order_by('-special')[:2]
        new_product = Product.objects.order_by('-create_date')[:8]
        context = {
           'categorys': categorys,
           'products': products,
           'sponsers': sponsers,
            'sizes': sizes,
            'user_corzina': user_corzina,
            'user_fav' : user_fav,
            'colors': colors,
           'pro_two': pro_two,
           'new_product' : new_product,
        }
        return render(request, 'shop.html', context)
    
    def search_view(request):
        search = request.GET.get('search', '')
        if search:
            search_products = Product.objects.filter(
                name__icontains=search) | Product.objects.filter(
                    category__icontains=search )| Product.objects.filter(description__icontains=search
            )
        else:
            search_products = Product.objects.none()  # Return an empty queryset if no search term is provided

        context = {
            'search_products': search_products,
            'search': search
        }
        return render(request, 'search.html', context)
    
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

        return redirect('shop')


class ShopDetailView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        products = Product.objects.all()
        sizes = Sizes.objects.all()
        choose_color = Choose_Color.objects.filter(product=product)
        colors = Colors.objects.all()
        '''userni aniqlash'''
        username = request.user.username
        user = User.objects.get(username=username)
        '''userni qanda izbraniga sox qigani'''
        user_fav = Favorite.objects.filter(user=user)
        user_fav = len(user_fav)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        user_corzina = Corzine.objects.filter(user=user)
        user_corzina = len(user_corzina)
        comment_user = Product.objects.order_by('-create_date')[:3]
        
        context = {
            'sizes': sizes,
            'colors': colors,
            'user_corzina': user_corzina,
            'user_fav' : user_fav,
            'comment_user':comment_user,
            'product':product,
            'products':products,
            'choose_color': choose_color,
        }
        return render(request, 'detail.html', context)
    
    def post(self, request, **kwargs):
        shop_id = kwargs.get('id') 
        '''kwargs id ni oqib oladi xato bermaslig uchun'''
        print(shop_id)
        my_fav = request.POST['favorite']
        if my_fav == 'favorite':
            product_name = request.POST['product_name']
            username = request.POST['username']
            product = Product.objects.get(name=product_name)
            user = User.objects.get(username=username)
            favorite = Favorite.objects.create(name=product, user=user)
            favorite.save()
        else:
            if my_fav == 'comment':
                product_name = request.POST['product_name']
                user = request.user
                text = request.POST.get('comment')
                comment = Comment.objects.create(text=text, customer=user)
                comment.save()
                product = Product.objects.get(name = product_name)
                product.comment.add(comment)
                product.save()
                return redirect('cart')
            else:
                product_name = request.POST['product_name']
                username = request.POST['username']
                product = Product.objects.get(name=product_name)
                user = User.objects.get(username=username)
                '''bu postdan request kelayotganini bilish uchun qoshildi!'''
                print(f"_________________{user}_______{product}")
                corzina = Corzine.objects.create(title=product, user=user)
                corzina.save()

        return redirect('shop')
    


class SearchListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search', '')
        print(f"___________________search_________________{search}")
        if search:
            search_products = Product.objects.filter(name__icontains=search)|Product.objects.filter(description__icontains=search)
        else:
            search_products = Product.objects.all() 
        context = {
            'search_products': search_products,
            'search': search
        }
        return render(request, 'search.html', context)
    

class CartListView(LoginRequiredMixin, View):
    def get(self, request):
        '''userni aniqlash'''
        username = request.user.username
        user = User.objects.get(username=username)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        corzines = Corzine.objects.filter(user=user)
        context = {
            'corzines' : corzines,
        }
        return render(request, 'cart.html', context)
    


class CartDeleteView(View):
    def get(self, request, id):
        corzines = Corzine.objects.get(id=id)
        corzines.delete()
        return redirect('cart')