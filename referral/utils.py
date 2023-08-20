import random
import re
import string
import time

from rest_framework import status
from rest_framework.response import Response

from referral.models import UserModel


def generate_verify_code() -> int:
    return random.randint(1000, 9999)


def generate_invite_code(length=6) -> str:
    characters = string.digits + string.ascii_letters
    invite_code = "".join(random.choice(characters) for _ in range(length))
    time.sleep(2)
    return invite_code


def activate_invite_code(request, invite_code):
    user_pk = request.user.pk
    user = UserModel.objects.get(pk=user_pk)
    search_invite_code = UserModel.objects.filter(invite_code=invite_code)
    if not search_invite_code:
        return Response(
            {"error": "This invite code is not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if user.activate_invite_code == "False":
        user.user_activate_code = invite_code
        user.activate_invite_code = True
        user.save()
    else:
        return Response(
            {"error": "You have already activated the invitation code."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(
        {"message": "This invite code has been successfully verified"},
        status=status.HTTP_200_OK,
    )


def checking_phone(phone: str):
    return re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", phone)


def delay_auth_code():
    time.sleep(2)
