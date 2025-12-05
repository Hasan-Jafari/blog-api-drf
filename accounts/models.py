from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils import timezone

from .managers import UserManager
from core.validators import validate_phone_number



class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[validate_phone_number],
        editable=False
    )
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.phone_number