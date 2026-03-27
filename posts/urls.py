from django.urls import path
from . import views 

urlpatterns =  [
    path('posts/', views.PostCreateListView.as_view(),  name='post-create-list'),
    path('posts/<uuid:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='business-detail-view')
]