from django.contrib import admin
from posts import models


class PostsAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_link', 'created_by', 'created_at',)
    search_fields = ('description', 'created_by', 'created_at',)

admin.site.register(models.Post, PostsAdmin)    