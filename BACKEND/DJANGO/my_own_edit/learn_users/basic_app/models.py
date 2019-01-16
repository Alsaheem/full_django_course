from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofileinfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional stuffs
    #portfolio link
    portfolio_link = models.URLField(blank=True)
    #profile pistue
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
