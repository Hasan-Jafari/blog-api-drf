import re
from rest_framework import serializers

from core.validators import validate_password



class SendOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    
    def validate_phone(self, value):
        if not re.match(r'^09\d{9}$', value):
            raise serializers.ValidationError("Phone Number Is Not Correct")
        return value
    

class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    

class SetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        validate_password(value)
        return value
