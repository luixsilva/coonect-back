from django.urls import path
from . import views

urlpatterns=[
    path('like/', views.LikeCreateListView.as_view(),  name='like-create-list'),
]