from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('read-post/<slug:slug>/', detail_view, name="post-detail"),
    path('my-posts/', all_my_posts, name="all-user-posts"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name="post-delete"),
]