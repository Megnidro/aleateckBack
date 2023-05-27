from email.headerregistry import Group
from django.db import models
from django.conf import settings
from datetime import date
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from services.models import SERVICES



from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Collaborateurs(AbstractUser):
    CIVILITE = [
        ('Mlle', 'Mlle'),
        ('M', 'M'),
        ('Mme', 'Mme')
    ]
    civilite = models.CharField(max_length=10, choices=CIVILITE)
    poste_occupe = models.CharField(max_length=15)
    implantation = models.CharField(max_length=30)
    numero_service = models.ForeignKey(SERVICES, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group, related_name='collaborateurs_set')
    user_permissions = models.ManyToManyField(Permission, related_name='collaborateurs_set')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', 'poste_occupe', 'phone_number']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

