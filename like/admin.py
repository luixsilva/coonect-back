from django.contrib import admin
from like import models


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user', 'post', 'uscreated_ater')

admin.site.register(models.Like, LikeAdmin)    