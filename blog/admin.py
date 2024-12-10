from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_time')
    search_fields = ('title', 'body', 'lead')
    list_filter = ('publish_time',)
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug': ('title',)}

