import re
from django.core.exceptions import ValidationError



def validate_password(value):
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])\S{8,}$', value):
        raise ValidationError('Your password is too weak.')
    return value