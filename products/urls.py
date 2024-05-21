from django.urls import path
from .views import HomePageView, ContactListView, UpdateListView


urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("contact/", ContactListView.as_view(), name='contact'),
    path('update/<int:id>/', UpdateListView.as_view(), name='product-update'),
]