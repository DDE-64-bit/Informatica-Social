# Generated by Django 5.0.1 on 2024-02-09 15:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="profileimg",
        ),
    ]