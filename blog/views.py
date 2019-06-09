from django.shortcuts import render
from .models import Post
from .models import Category

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

def view(request, slug):
    context = Post.objects.filter(category__in=Category.objects.filter(title=slug))
    context_dict = {
         'posts': context
    }
    return render(request, 'blog/post_list.html', context_dict)

def details(request):
	return render(request, 'blog/post_details.html')