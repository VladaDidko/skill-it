from django.urls import path
from . import views

urlpatterns = [
    path('blog/posts', views.home),
    path('blog/category/<slug:slug>/', views.view),
    path('blog/post_details', views.details)
]