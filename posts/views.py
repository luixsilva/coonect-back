from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Count, Exists,OuterRef
from like.models import Like

class PostCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user

        return Post.objects.all().annotate(
            likes_count=Count("likes"),
            liked_by_user=Exists(
                Like.objects.filter(
                    post=OuterRef('pk'),
                    user=user
                )
            )
        )

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer