from django.urls import path
from post import views

urlpatterns = [
    path("", views.home, name="index"),
    path('home', views.home, name="home"),
    path('upload', views.upload_view, name="upload_view"),
    path('explore', views.explore_view, name='explore'),
    path('notifications', views.notification_view, name="notifications"),
    path('search', views.search_user_view, name="search"),
    path('user/<str:search_user>', views.user_view, name="user"),
    path('post/<str:post_id>', views.post_view, name="post"),
    path('posts', views.posts, name="posts"),
    path('like-post/', views.like_post_view, name="like-post"),
    path('comment/', views.comment_view, name="comment"),
]
