from django.urls import path
from . import views

urlpatterns = [
    path('blog/posts', views.home),  
]