from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
  user = models.ForeignKey(User, related_name="tweets", on_delete=models.DO_NOTHING)
  content = models.TextField(max_length=180, blank=True)
  tweet_date = models.DateField(auto_now_add=True)
  tweet_image = models.ImageField(null=True, blank=True, upload_to="images/tweets")
  likes = models.ManyToManyField(User, related_name="tweet_like", blank=True)

  def like_amount(self):
    return self.likes.count()
