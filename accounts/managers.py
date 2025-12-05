from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

from core.validators import validate_phone_number



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password):
        if not phone_number:
            raise ValidationError('Phone number is required.')
        
        validate_phone_number(phone_number)
        user = self.model(phone_number=phone_number)
        
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        
        user.is_staff = False
        user.is_active = False
        user.is_active = True
        user.is_superuser = False
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password):
        if not password:
            raise ValueError('Superuser must have a password.')
        user = self.create_user(
            phone_number=phone_number,
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user