import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(null=True, blank=True)
    image_link = models.CharField(null=True, blank=True)
    created_by = models.CharField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_clerk_id = models.CharField()
    
    class Meta:
        verbose_name_plural = 'posts'