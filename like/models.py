from django.db import models
from posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural = 'likes'
        unique_together = ('post', 'user')