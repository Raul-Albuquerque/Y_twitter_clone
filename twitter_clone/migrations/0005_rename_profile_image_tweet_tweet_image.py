# Generated by Django 5.0.3 on 2024-03-29 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("twitter_clone", "0004_tweet_profile_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tweet",
            old_name="profile_image",
            new_name="tweet_image",
        ),
    ]
