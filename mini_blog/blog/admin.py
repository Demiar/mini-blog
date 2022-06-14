from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'post_date')
    list_display_links = ('id', 'title')
    list_filter = ['post_date']
    search_fields = ('id', 'title', 'author__username')

admin.site.register(Blog, BlogAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['id', 'user__username']

admin.site.register(Author, AuthorAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'blog']
    search_fields = ['id', 'author__username', 'blog__title']

admin.site.register(Comment, CommentAdmin)


