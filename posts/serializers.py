from rest_framework import serializers
from posts.models import Post
from user.serializer import UserSerializer

class PostSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)
        likes_count = serializers.IntegerField(read_only=True)
        liked_by_user = serializers.BooleanField(read_only=True)

        class Meta: 
            model = Post
            fields = '__all__'
            read_only_fields = ["user"] 