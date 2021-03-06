from django.shortcuts import render, redirect

from blog.models import Post
from users.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from users.models import Follower
from blog.forms import PostForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'The account has been created!You may log in now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')

@login_required
def user_details(request, pk):
    user = User.objects.all().get(id=pk)
    context = {
        'user': user,
        'posts': Post.objects.all(),
        'followers': Follower.objects.all()
    }
    return render(request, 'users/user_details.html', context)

@login_required
def update_status(request, pk):
  action = request.POST.get('sbr', '')

  if action == 'Follow':
    following = User.objects.get(id=pk)
    follower = Follower(follower=request.user, following=following)
    follower.save()
  else:
    following = User.objects.get(id=pk)
    Follower.objects.filter(follower=request.user, following=following).delete()

  user = User.objects.all().get(id=pk)
  context = {
        'user': user,
        'followers': Follower.objects.all()
    }
  return render(request, 'users/user_details.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit_profile.html', context)


@login_required
def my_posts(request):
    user=request.user
    myposts = Post.objects.filter(author=request.user)
    context = {
        'myposts':myposts,
    }
    return render(request, 'users/my_posts.html', context)

@login_required
def del_post(request, pk):
    Post.objects.get(pk=pk).delete()
    myposts = Post.objects.filter(author=request.user)
    context = {
        'myposts': myposts
    }
    return render(request, 'users/my_posts.html', context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'category', 'image', 'videofile']

    def get_success_url(self):
            return reverse('mypost_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'category', 'image', 'videofile']

    def get_success_url(self):
            return reverse('mypost_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)