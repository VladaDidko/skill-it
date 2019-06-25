from datetime import timezone

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return  self.title

class Subcategory(models.Model):
	title = models.CharField(max_length=200)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)

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
	likes= models.IntegerField(default=0)
	dislikes= models.IntegerField(default=0)


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
    date_commented = models.DateTimeField(auto_now=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Preferance(models.Model):
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    value= models.IntegerField()
    date= models.DateTimeField(auto_now= True)

    
    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
       unique_together = ("user", "post", "value")
