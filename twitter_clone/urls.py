from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, like_tweet_view, signup_view, signin_view, feed_tweets_view, feed_profile_view, logout_view, delete_tweet_view

urlpatterns = [
    path("", home_view.home, name="home"),
    path("signup/", signup_view.signup, name="signup"),
    path("signin/", signin_view.signin, name="signin"),
    path("feed/", feed_tweets_view.feed_tweets, name="feed_tweets"),
    path("profile/", feed_profile_view.feed_profile, name="profile"),
    path("like_tweet/<int:pk>", like_tweet_view.like_tweet, name="like_tweet"),
    path("logout/", logout_view.user_logout, name="logout"),
    path("delete_tweet/<int:pk>", delete_tweet_view.delete_tweet, name="delete_tweet")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
