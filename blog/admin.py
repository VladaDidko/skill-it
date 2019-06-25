from django.contrib import admin
from .models import Comment, Preferance, Subcategory

# Register your models here.
admin.site.register(Comment)
admin.site.register(Preferance)
admin.site.register(Subcategory)