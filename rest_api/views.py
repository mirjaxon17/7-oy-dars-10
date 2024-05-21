from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from products.models import Comment, Category, Sizes, Colors, Product, Choose_Color, Sponser, Favorite, Corzine, Special
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer, SpecialSerializer, CategorySerializer, SizeSerializer,ColorSeriazlizer,ProductSerializer, ChooseColorSerializer, SponserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status, permissions
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response


class CommentDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['text', ]
    pagination_class = LimitOffsetPagination

class SpecialDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination


class CategoryDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title', 'description', 'special']
    pagination_class = LimitOffsetPagination

class SizeDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Sizes.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', ]
    pagination_class = LimitOffsetPagination

class ColorDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Colors.objects.all()
    serializer_class = ColorSeriazlizer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name',]
    pagination_class = LimitOffsetPagination

class ProductDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name','comment', 'description', 'category', 'size', 'price','price_type', 'sale_price','how_many']
    pagination_class = LimitOffsetPagination

class ChooseColorDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Choose_Color.objects.all()
    serializer_class = ChooseColorSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['product','color']
    pagination_class = LimitOffsetPagination


class SponserDetailApiView(ModelViewSet,LoginRequiredMixin):
    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name',]
    pagination_class = LimitOffsetPagination