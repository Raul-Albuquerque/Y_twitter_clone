# Generated by Django 5.0.3 on 2024-03-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twitter_clone", "0006_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/profiles"),
        ),
    ]
