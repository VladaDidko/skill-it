from django.shortcuts import render
from blog.models import Category
from django.http import HttpResponse
from users.models import Profile, Follower
from django.contrib.auth.models import User

def home(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'general/base.html', context)

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