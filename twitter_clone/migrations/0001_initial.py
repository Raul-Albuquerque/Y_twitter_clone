# Generated by Django 5.0.3 on 2024-03-19 02:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("bio", models.TextField(blank=True, max_length=180)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "follows",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followed_by",
                        to="twitter_clone.profile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tweet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(blank=True, max_length=180)),
                ("tweet_date", models.DateTimeField(auto_now_add=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="tweet_like",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="tweets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
