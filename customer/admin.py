from django.contrib import admin
from products.models import Corzine, Favorite, Comment, Colors, Sizes
from import_export.admin import ImportExportActionModelAdmin



@admin.register(Corzine)
class Backade(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title', 'user')
    search_fields = ('title', 'user', 'id')
    ordering = ('id',)

@admin.register(Favorite)
class FavoriteAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name', 'user')
    search_fields = ('name', 'user', 'id')
    ordering = ('id',)

@admin.register(Comment)
class CommentAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'text_obj', 'customer')
    list_display_links = ('id', 'text_obj', 'customer')
    search_fields = ('text_obj', 'customer', 'id')
    ordering = ('id',)

    def text_obj(self, obj):
        return obj.text[:5]


