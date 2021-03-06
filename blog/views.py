from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Preferance
from .forms import CommentForm, PostForm
from .models import Category, Subcategory
import random
from django.db.models import Q
from users.models import Profile
from django.contrib.auth.models import User
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
        return Category.objects.filter(category=category)

class SubcategoryView(generic.ListView):
    model = Subcategory
    template_name="general/base.html"
    context_object_name = 'all_subcategories'
    category = Category.objects.all()

    def get_queryset(self):
        return Subcategory.objects.all()

def home(request):
    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
    'categories': Category.objects.all(),
    }

    return render(request, 'general/home.html', context)

def post_list(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)



def post_list_new(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-published_date')

    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)

def post_list_popular(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-likes')
    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)


def post_list_recommended(request):
    current_user = request.user
    obj = Profile.objects.get(user__in=User.objects.filter(id=current_user.id))
    skills = obj.skills.split(',')
    for i, x in enumerate(skills):
        skills[i] = x.replace(' ', '')
        skills[i] = skills[i].title()

    empty = True
    recommended = []


    AllCategories = Category.objects.all();
    for x in AllCategories:
        for y in skills:
            if x.title == y:
                empty = False
                recommended.append(y)   

    if empty == True:
        posts = Post.objects.all()
    else:
        category = random.choice(recommended)
        posts = Post.objects.all().filter(category__in=Category.objects.filter(title=category))

    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
        'categories': AllCategories,
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)

def category_list(request, slug):
    posts = Post.objects.filter(category__in=Category.objects.filter(title=slug))
    
    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) |
            Q(text__icontains=query) |
            Q(category__title__icontains=query) |
            Q(author__username__icontains=query)).distinct()
    context = {
         'posts': posts
    }

    return render(request, 'blog/post_list.html', context)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})

def mypost_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/mypost_detail.html', {'post': post})


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

@login_required
def postpreference(request, pk, id):
    if request.method == "POST":
        post= get_object_or_404(Post, pk=pk)
        obj=''
        valueobj=''
        try:
            obj= Preferance.objects.get(user=request.user, post=post)
            valueobj= obj.value #value of id
            valueobj= int(valueobj)
            id= int(id)
            if valueobj != id:
                obj.delete()
                upref= Preferance()
                upref.user= request.user
                upref.post= post
                upref.value= id
                if id == 1 and valueobj != 1:
                    post.likes += 1
                    post.dislikes -=1
                elif id == 2 and valueobj != 2:
                    post.dislikes += 1
                    post.likes -= 1
                upref.save()
                post.save()
                context= {'post': post, 'pk': pk}

                return render (request, 'blog/post_details.html', context)
            elif valueobj == id:
                obj.delete()
                if id == 1:
                    post.likes -= 1
                elif id == 2:
                    post.dislikes -= 1
                post.save()
                context= {'post': post, 'pk': pk}

                return render (request, 'blog/post_details.html', context)

        except Preferance.DoesNotExist:
            upref= Preferance()
            upref.user= request.user
            upref.post= post
            upref.value= id
            id=int(id)
            if id == 1:
                post.likes += 1
            elif id == 2:
                post.dislikes +=1
            upref.save()
            post.save()
            context= {'post': post,'pk': pk}
            return render (request, 'blog/post_details.html', context)

        else:
            post= get_object_or_404(Post, pk=pk)
            context= {'post': post, 'pk': pk}
            return render (request, 'blog/post_details.html', context)