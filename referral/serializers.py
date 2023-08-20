from rest_framework import serializers

from referral.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("phone", "password", "verify_code")
        extra_kwargs = {
            "password": {"write_only": True},
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            "invite_code",
            "phone",
        )
