from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import generics
from like.models import Like
from like.serializers import LikeSerializer


class LikeCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)