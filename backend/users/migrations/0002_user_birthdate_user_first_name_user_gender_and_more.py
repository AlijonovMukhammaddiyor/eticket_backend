# Generated by Django 4.1.9 on 2023-06-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=255, verbose_name="First Name of User"),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_organizer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=255, verbose_name="Last Name of User"),
        ),
    ]
