from rest_framework import serializers
from like.models import Like
from user.serializer import UserSerializer


class LikeSerializer(serializers.ModelSerializer): 
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ["user"] 
