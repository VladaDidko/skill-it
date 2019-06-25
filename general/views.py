from django.shortcuts import render
from blog.models import Category, Post
from django.http import HttpResponse
from users.models import Profile, Follower
from django.contrib.auth.models import User

def home(request):
	current_user = request.user
	followers = Follower.objects.all().filter(follower__in=User.objects.filter(id=current_user.id))
	context = {
	    'categories': Category.objects.all(),
        'posts': Post.objects.all(),
        'followers': followers
	}
	return render(request, 'general/home.html', context)

def users(request):
	context = {
		'users': User.objects.all(),
		'profiles': Profile.objects.all(),
		'followers': Follower.objects.all(),
	}
	return render(request, 'general/people.html', context)


def followers(request):
	current_user = request.user
	followers = Follower.objects.all().filter(following__in=User.objects.filter(id=current_user.id))
	context = {
		'followers': followers
	}
	return render(request, 'general/followers.html', context)

def following(request):
	current_user = request.user
	followers = Follower.objects.all().filter(follower__in=User.objects.filter(id=current_user.id))
	context = {
		'followers': followers
	}
	return render(request, 'general/following.html', context)

def update(request, pk):
	following = User.objects.get(id=pk)
	follower = Follower(follower=request.user, following=following)
	follower.save()

	context = {
		'users': User.objects.all(),
		'profiles': Profile.objects.all(),
		'followers': Follower.objects.all(),
	}
	return render(request, 'general/people.html', context)