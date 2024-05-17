from django.contrib import admin
from .models import Category, Product, Sponser
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title', 'image')
    search_fields = ('name', 'id')
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name', 'description', 'price')
    search_fields = ('name', 'id')
    ordering = ('id',)
@admin.register(Sponser)
class SponserAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name', 'image')
    search_fields = ('name', 'id')
    ordering = ('id',)



    
