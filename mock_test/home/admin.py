from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'user']
    list_filter = ['title', 'created_at', 'user']
    search_fields = ['title', 'created_at', 'user']
admin.site.register(Post, PostAdmin)
