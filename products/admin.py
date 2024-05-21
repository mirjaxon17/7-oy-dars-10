from django.contrib import admin
from .models import Category, Product, Sizes, Colors, Choose_Color, Sponser, Special
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

@admin.register(Sizes)
class SizeAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id',)


@admin.register(Colors)
class ColorAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id',)
    
@admin.register(Sponser)
class SponserAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id',)

@admin.register(Choose_Color)
class ChooseColorAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')
    search_fields = ('product', 'id')
    ordering = ('id',)


@admin.register(Special)
class SpecialAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id',)





    
