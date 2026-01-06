from django.urls import path
from .views import  PostListView, PostDetailView, createPost, updatePost, deletePost, UserPostListView

from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', createPost.as_view(), name='post-create'),
    path('post/<int:pk>/update/', updatePost.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', deletePost.as_view(), name='post-delete'),
    
]