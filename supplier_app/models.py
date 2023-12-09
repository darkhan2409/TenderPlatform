from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import SupplierManager


class Supplier(AbstractBaseUser, PermissionsMixin):
    title = models.CharField(max_length=256, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    bin = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = SupplierManager()

    def __str__(self):
        return self.username

