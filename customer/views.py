from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Comment, Category, Sizes, Colors, Product, Choose_Color, Sponser, Favorite, Corzine, Special
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



class UserRegistorView(View):
    def get(self, request):
        return render(request, 'log_tem/registor.html')
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        replay_password = request.POST['replay_password']
        if password == replay_password:
            user = User(first_name=first_name, last_name= last_name, email=email, username=username)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'log_tem/registor.html')
            
                
    
class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'log_tem/index.html', {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        data = {
            'username': username,
            'password' : password
        }

        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        
        else:
            form = UserLoginForm()
            context={
                'form':form
            }
            return render(request, 'log_tem/registor.html', context)
        
class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    


class FavoriteListView(LoginRequiredMixin, View):
    def get(self, request):
        '''userni aniqlash'''
        username = request.user.username
        user = User.objects.get(username=username)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        favorite = Favorite.objects.filter(user=user)
        product = Product.objects.all()
        context = {
            'corzines' : favorite,
            'product': product,
        }
        return render(request, 'my_favorite.html', context)
    

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
    

class FavoriteDeleteView(View):
    def get(self, request, id):
        favorites = Favorite.objects.get(id=id)
        favorites.delete()
        return redirect('favorite')

class CheckoutListVies(LoginRequiredMixin, View):
    def get(self, request):
        '''userni aniqlash'''
        username = request.user.username
        user = User.objects.get(username=username)
        '''user qancha narsani savatga saqlagani xaqida malumot'''
        corzines = Corzine.objects.filter(user=user)
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
       
        context = {
            'corzines' : corzines,
        }
        return render(request, 'checkout.html', context)

            

