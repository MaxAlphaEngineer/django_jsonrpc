#  Unisoft Group Copyright (c) 2022/12/5
#
#  Created by Muzaffar Makhkamov
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from v1.models.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), unique=True, max_length=50)

    is_test = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    identity = models.CharField(max_length=3, default='TT')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "1. Users"

    objects = CustomUserManager()
    pass


class AccessToken(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_token")
    key = models.CharField(max_length=128)

    def generate(self):
        self.key = f"{uuid.uuid4()}/{uuid.uuid4()}"
        self.save()
        return self.key


class Service:
    pass


class UserServicePermissions:
    pass
