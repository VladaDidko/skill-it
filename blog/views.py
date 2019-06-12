from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from .models import Category
from django.views import generic
from django.views.generic import ListView, View
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


class CategoryView(generic.ListView):
    model = Category
    template_name = 'general/base.html'
    context_object_name = 'all_categories'

   
    def get_queryset(self):
        return Category.objects.all()


def home(request):
    context = {
    'categories': Category.objects.all(),
    }

    return render(request, 'general/home.html', context)

def post_list(request):
    context = {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
    }
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(category__icontains = query) 
            ).distinct()
        
    return render(request, 'blog/post_list.html', context)

def view(request, slug):
    context = Post.objects.filter(category__in=Category.objects.filter(title=slug))
    context_dict = {
         'posts': context
    }
    return render(request, 'blog/post_list.html', context_dict)


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_details', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_details', pk=comment.post.pk)
