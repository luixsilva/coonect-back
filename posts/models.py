import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(null=True, blank=True)
    image_link = models.CharField(null=True, blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural = 'posts'
        ordering = ['-created_at'] 