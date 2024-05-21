from django.urls import path
from .views import ShopListView, ShopDetailView, CartListView, CartDeleteView, SearchListView

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop'),
    path('shop-detail/<int:id>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shop/cart/', CartListView.as_view(), name='cart'),
    path('shop/cart/delete/<int:id>/', CartDeleteView.as_view(), name='cart-delete'),
    path('search/', SearchListView.as_view(), name='search-page'),
]