# Generated by Django 4.2.4 on 2023-08-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("referral", "0003_usermodel_user_activate_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="user_activate_code",
            field=models.CharField(default="000000", max_length=6),
        ),
    ]