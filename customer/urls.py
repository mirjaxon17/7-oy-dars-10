from django.urls import path
from .views import UserRegistorView, UserLoginView, UserLogOutView, FavoriteListView, FavoriteDeleteView, CheckoutListVies

urlpatterns = [
    path('register/', UserRegistorView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('my_favorite/', FavoriteListView.as_view(), name='favorite'),
    path('shop/favorite/delete/<int:id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
    path('shop/checkout/', CheckoutListVies.as_view(), name='checkout'),
]