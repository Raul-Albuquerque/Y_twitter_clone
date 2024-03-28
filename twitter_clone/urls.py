from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, signup_view, signin_view, feed_view, feed_tweets_view, feed_profile_view, like_tweet

urlpatterns = [
    path("", home_view.home, name="home"),
    path("signup/", signup_view.signup, name="signup"),
    path("signin/", signin_view.signin, name="signin"),
    path("feed/", feed_tweets_view.feed_tweets, name="feed_tweets"),
    path("profile/", feed_profile_view.feed_profile, name="profile"),
    path("like_tweet/<int:pk>", like_tweet.like_tweet, name="like_tweet"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
