from django.shortcuts import render
from blog.models import Category
from django.http import HttpResponse

def home(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'general/base.html', context)