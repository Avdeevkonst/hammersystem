from rest_framework.authentication import BaseAuthentication

from referral.models import UserModel


class PhoneAuthentication(BaseAuthentication):
    def authenticate(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")
        if not phone_number or not password:
            return None
        try:
            user = UserModel.objects.get(phone=phone_number)
            if user.check_password(password):
                return user, None
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
