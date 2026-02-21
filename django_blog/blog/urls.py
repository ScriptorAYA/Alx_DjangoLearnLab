from django.urls import path
from .views import add_comment, update_comment, delete_comment
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
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', add_comment, name='add-comment'),
path('comment/<int:pk>/update/', update_comment, name='update-comment'),
path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),

]

