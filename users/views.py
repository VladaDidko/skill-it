from django.shortcuts import render, redirect

from blog.models import Post
from users.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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
        'user': user
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text', 'category', 'image', 'videofile']

    def get_success_url(self):
            return reverse('mypost_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)