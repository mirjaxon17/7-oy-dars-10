from django.urls import path
from .views import UserRegistorView, UserLoginView, UserLogOutView

urlpatterns = [
    path('register/', UserRegistorView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]