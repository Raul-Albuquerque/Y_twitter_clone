# Generated by Django 5.0.3 on 2024-03-26 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter_clone", "0002_auto_20240326_0013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="tweet_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
