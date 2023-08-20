from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from referral.authenticate import PhoneAuthentication
from referral.models import UserModel
from referral.serializers import ProfileSerializer, UserSerializer
from referral.utils import (
    activate_invite_code,
    checking_phone,
    generate_invite_code,
    generate_verify_code,
)


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [PhoneAuthentication]

    def post(self, request):
        phone_number = request.data.get("phone")
        password = request.data.get("password")
        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = UserModel.objects.filter(phone=phone_number).first()
        verify_code = generate_verify_code()
        if not user:
            invite_code = generate_invite_code()
            user = UserModel(
                phone=phone_number,
                invite_code=invite_code,
                verify_code=verify_code,
                password=password,
            )
            status_code = status.HTTP_201_CREATED
        else:
            user.verify_code = verify_code
            status_code = status.HTTP_200_OK
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status_code)


class VerifyCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone")
        verification_code = request.data.get("verify_code")
        if not phone_number or not verification_code:
            return Response(
                {"error": "Phone number and verification code are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if checking_phone(str(phone_number)):
            user = UserModel.objects.filter(phone=phone_number).first()
            if not user:
                return Response(
                    {"error": "User not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            if str(verification_code) != str(user.verify_code):
                return Response(
                    {"error": "Verification code is incorrect."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.is_active = True
            user.save()
            login(request, user, "referral.authenticate.PhoneAuthentication")
        else:
            return Response(
                {"error": "Phone number is uncorrected."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"message": "user successfully sign in.", "your id": user.id},
            status=status.HTTP_200_OK,
        )


class Profile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        user = UserModel.objects.filter(pk=pk)
        if not user:
            return Response(
                {"error": "This user does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        used_code = UserModel.objects.filter(user_activate_code=user.invite_code)
        phone_numbers = [user.phone for user in used_code]
        if len(phone_numbers) < 1:
            phone_numbers = "No one has entered your code yet."
        if user.activate_invite_code:
            user_activate_code_response = user.user_activate_code
            return Response(
                {
                    "phone_numbers": phone_numbers,
                    "user_activate_code_response": user_activate_code_response,
                },
            )
        return Response(
            {
                "phone_numbers": phone_numbers,
                "invite_code": user.invite_code,
            },
        )

    def post(self, request):
        return activate_invite_code(
            request,
            invite_code=request.data.get("invite_code"),
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})
