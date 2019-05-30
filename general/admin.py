from django.contrib import admin
from blog.models import Category
from blog.models import Post
from users.models import Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Post)