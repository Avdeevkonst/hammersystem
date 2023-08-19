from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("user must have a phone.")
        user = self.model(
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(
            phone=phone,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(
        help_text="Укажите номер телефона в формате 79001005070.",
        unique=True,
        editable=False,
        max_length=12,
    )
    invite_code = models.CharField(default="000000", max_length=6)
    activate_invite_code = models.BooleanField(default=False)
    user_activate_code = models.CharField(default="000000", max_length=6)
    verify_code = models.CharField(default="0000", max_length=4)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"

    def __str__(self):
        return str(self.phone)
