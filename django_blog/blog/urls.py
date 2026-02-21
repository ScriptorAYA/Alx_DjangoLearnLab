from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag, PostByTagListView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
path('search/', search_posts, name='search-posts'),
path('search/', search_posts, name='search-posts'),
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),


]

