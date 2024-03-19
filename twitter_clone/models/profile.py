from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
  profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
  bio = models.TextField(max_length=180, blank=True)
  creation_date = models.DateTimeField(auto_now_add=True)