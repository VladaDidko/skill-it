"""skill_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from general import views as main_views
from users import views as user_views
from users.views import PostCreateView, PostUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', user_views.profile, name='profile'),
    path('user_details/<int:pk>/', user_views.user_details, name='user_details'),
    path('user/<int:pk>/', user_views.update_status, name='update_status'),
    path('edit_profile/', user_views.edit_profile, name = 'edit_profile'),
    path('my_posts/', user_views.my_posts, name='my_posts'),
    path('my_posts/deleted/<int:pk>/updated/', user_views.del_post, name='del_post'),
    path('my_posts/edit/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('my_posts/new', PostCreateView.as_view(), name='post-create'),
    path('people/', main_views.users, name='people'),
    path('people/following/<int:pk>/', main_views.update, name='update'),
    path('profile/followers', main_views.followers, name='followers'),
    path('profile/following', main_views.following, name='following'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

