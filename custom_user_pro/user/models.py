from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password, user_type, is_staff=False, is_active=True, is_superuser=False, **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, password=password, user_type=user_type, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, is_staff=True, is_active=True, is_superuser=True, **extra_fields):
        return self.create_user(email, password, is_staff, is_active, is_superuser, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    user_type = models.SmallIntegerField(
        blank=False, null=False, default=1, choices=[
            (1, 'admin'), (2, 'superuser'), (3, 'user')
        ])

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f'{self.email} - {self.full_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
        get_latest_by = 'date_joined'