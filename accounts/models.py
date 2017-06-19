from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
from department.models import Department
from review.models import Review
from django.conf import settings

from django.core.validators import RegexValidator

EMAIL_REGEX = '^[a-z0-9](\.?[a-z0-9]){5,}@aiesec\.net$'
USERNAME_REGEX = '^[a-zA-Z0-9.@+_]*$'

class UserManager(BaseUserManager):
    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not display_name:
            display_name = username

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            display_name=display_name,
            department=Department.objects.get(id=1)

        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, display_name, password):
        user = self.create_user(
            email,
            username,
            display_name,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True,max_length=255,
    blank=False,
     validators=[RegexValidator( regex = EMAIL_REGEX,
     message='Email must end with @aiesec.net',
     code='invalid email')])
    username = models.CharField(max_length=40,blank=False,
    unique=True,
    validators=[RegexValidator( regex = USERNAME_REGEX,
     message='username must be alphanumeric or contain ., @, +, _',
     code='invalid_username')])
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    display_name = models.CharField(max_length=140)
    bio = models.TextField(max_length=500, blank=True, default="")
    avatar = models.ImageField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    review = models.ManyToManyField('self', through=Review,
    related_name='testinomial', symmetrical=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["display_name", "email"]

    def __str__(self):
        return "@{}".format(self.username)

    def get_short_name(self):
        return self.display_name

    def get_long_name(self):
        return "{} (@{})".format(self.display_name, self.username)
