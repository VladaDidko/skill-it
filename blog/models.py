from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return  self.title

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(blank=True)
	image = models.ImageField(upload_to='post_pics', blank=True)
	videofile = models.FileField(upload_to='post_vid', blank=True)
	published_date = models.DateTimeField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title