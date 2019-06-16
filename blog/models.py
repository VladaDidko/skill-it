from datetime import timezone

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return  self.title

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(blank=True)
	image = models.ImageField(upload_to='profile_pics', blank=True)
	videofile = models.FileField(upload_to='post_vid', blank=True)
	published_date = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def publish(self):
		self.save()

	def __str__(self):
		return self.title

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text