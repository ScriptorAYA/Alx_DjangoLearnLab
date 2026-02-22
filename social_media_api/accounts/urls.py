from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, ListUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("users/", ListUsersView.as_view(), name="list-users"),  # list all users
    path("users/<int:user_id>/follow/", FollowUserView.as_view(), name="follow-user"),
    path("users/<int:user_id>/unfollow/", UnfollowUserView.as_view(), name="unfollow-user"),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

