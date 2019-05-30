from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache 
from PIL import Image
from datetime import datetime
from skill_it import settings



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.CharField(max_length=500)
    date_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=200)

    
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    	
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='Ч')
    skills = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'

    def last_seen(self):
    	return cache.get('seen_%s' % self.user.username)

    def online(self):
    	if self.last_seen():
    		now = datetime.datetime.now()
    		if now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
    			return False
    		else:
    			return True
    	else: return False

