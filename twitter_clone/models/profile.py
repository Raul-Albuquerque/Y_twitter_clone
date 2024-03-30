from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
  profile_image = models.ImageField(null=True, blank=True, upload_to="images/profiles")
  bio = models.TextField(max_length=180, blank=True)
  creation_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

def create_profile(sender, instance, created, **kwargs):
  if created:
    user_profile = Profile(user=instance)
    user_profile.save()
    user_profile.follows.set([instance.profile.id])
    user_profile.save()

post_save.connect(create_profile, sender=User)