from django.urls import path
from . import views

urlpatterns = [
    path('blog/posts', views.post_list, name='post_list'),
    path('blog/category/<slug:slug>/', views.view, name='category_list'),
    path('blog/category/post/<int:pk>/', views.post_details, name='post_details'),
    path('my_posts/<int:pk>/', views.mypost_detail, name='mypost_detail'),
    path('post/category/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('blog/category/post/<int:pk>/preferance/<int:id>/', views.postpreference, name='postpreference'),

    
]