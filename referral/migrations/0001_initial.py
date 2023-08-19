# Generated by Django 4.2.4 on 2023-08-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserModel",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "phone",
                    models.CharField(
                        editable=False,
                        help_text="Укажите номер телефона в формате 79001005070.",
                        max_length=12,
                        unique=True,
                    ),
                ),
                ("invite_code", models.CharField(default="000000", max_length=6)),
                ("activate_invite_code", models.BooleanField(default=False)),
                (
                    "user_activate_code",
                    models.CharField(default="000000", max_length=6),
                ),
                ("verify_code", models.CharField(default="0000", max_length=4)),
                ("is_active", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
