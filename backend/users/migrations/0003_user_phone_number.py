# Generated by Django 4.1.9 on 2023-06-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_birthdate_user_first_name_user_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
