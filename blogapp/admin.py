from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = (
        'tittle','content', 'date', 'author' 
    )
    list_filter= (
        'date', 'author'
    )
