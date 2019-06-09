from django.shortcuts import render
from .models import Post
from .models import Category
from django.views import generic
from django.views.generic import ListView, View

# Create your views here.


class CategoryView(generic.ListView):
    model = Category
    template_name = 'general/base.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


def home(request):
    return render(request, 'general/home.html', context)

def post_list(request):
    context = {
        'categories': Category.objects.all(),
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