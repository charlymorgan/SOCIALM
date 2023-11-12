from django.db import models

# Create your models here.

from datetime import date
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_pics = models.ImageField(upload_to="profile_images", 
                                     default="blank-profile-photo.jpeg")
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class FollowerCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()