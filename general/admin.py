from django.contrib import admin
from blog.models import Category
from users.models import Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Profile)