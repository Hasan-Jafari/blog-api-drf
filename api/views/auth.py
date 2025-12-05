from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions

from accounts.models import User
from core.serializers.auth import SetPasswordSerializer
from core.serializers import SendOtpSerializer, VerifyOtpSerializer
from utils import generate_otp_code, set_value, get_value, delete_value



class SendOtpTokenApi(APIView):
    serializer_class = SendOtpSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = SendOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone', None)
            otp = generate_otp_code()
            set_value(f"otp:{phone}", otp, ttl=3600)
            
            return Response(
                {"message": "OTP SEND", "DEBUG": (otp, phone)},
                status=status.HTTP_200_OK
            )
        return Response(
            {"message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
            

class VerifyOtpTokenApi(APIView):
    serializer_class = VerifyOtpSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        phone = request.headers.get("X-PHONE")
        serializer = VerifyOtpSerializer(data=request.data)
        
        if serializer.is_valid():
            otp = serializer.validated_data.get('otp')
            if not phone or not otp:
                return Response(
                    {"error": "phone_number or otp is invalid"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            save_otp = get_value(f"otp:{phone}")
            
            if save_otp != otp:
                return Response(
                    {"error": "Otp is Invalid or expired"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            user, created = User.objects.get_or_create(phone_number=phone)
            if not user.is_active:
                user.is_active = True
                user.save()
    
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            
            delete_value(f'otp:{phone}')
            
            return Response({
                'access': str(access),
                'refresh': str(refresh),
                'user': str(user.phone_number)
            })



class SetPasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = SetPasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        user = request.user
        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()

        return Response({
            "message": "Your password has been successfully set."},
            status=status.HTTP_200_OK
        )