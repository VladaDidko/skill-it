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