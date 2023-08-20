from django.urls import path

from referral.views import LoginView, LogoutView, Profile, VerifyCodeView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("verify/", VerifyCodeView.as_view(), name="verify"),
    path("profile/", Profile.as_view(), name="profile"),
    path("profile/<int:pk>", Profile.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
