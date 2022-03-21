from django.urls import path

from .views import SignupAPIView, UserAPIView, VerificationAPIView

urlpatterns = [
    path('v1/auth/signup/', SignupAPIView.as_view(), name='signup'),
    path(
        'v1/auth/signup/verify/',
        VerificationAPIView.as_view(),
        name='verification'
        ),
    path('v1/me/', UserAPIView.as_view(), name='account'),
]
