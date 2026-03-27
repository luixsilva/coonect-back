from django.contrib import admin
from posts import models


class PostsAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_link', 'created_at', 'user')
    search_fields = ('description', 'created_at', 'user')

admin.site.register(models.Post, PostsAdmin)    