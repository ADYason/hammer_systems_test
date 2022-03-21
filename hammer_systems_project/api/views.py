import time

from rest_framework import permissions, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .generator import code_generator
from .models import User
from .permissions import Verified
from .serializers import SignupSerializer, UserSerializer, ValidateSerializer


def confirmation_sms(user):
    """Эмуляция отправки кода подтверждения.
    Я не знаю каким образом будет отправляться смс-подтверждение.
    Как это примерно должно выглядеть."""
    # phone_number = user.phone_number
    # confirmation_code = user.confirmation_code
    # send_sms(
    # to=phone_number,
    # message=f' Ваш код подтверждения - {confirmation_code}',
    # from=<сервис организации>
    # )
    time.sleep(1)
    pass


class SignupAPIView(views.APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = SignupSerializer

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            user = get_object_or_404(User, phone_number=phone_number)
            confirmation_sms(user)
            refresh = RefreshToken.for_user(user)
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {
                'message': 'Код активации повторно направлен в смс.',
                'token': str(refresh.access_token)
            }
            return response
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(phone_number=phone_number)
        confirmation_code = code_generator(4)
        User.objects.filter(
            phone_number=phone_number).update(
                confirmation_code=confirmation_code)
        confirmation_sms(user)
        refresh = RefreshToken.for_user(user)
        response = Response(status=status.HTTP_201_CREATED)
        response.data = {
            'message': f'Пользователь успешно создан - код подтверждения: {confirmation_code}',  # кода подтверждения не будет, код будет получен из смс
            'token': str(refresh.access_token)
        }
        return response


class VerificationAPIView(views.APIView):

    serializer_class = ValidateSerializer

    def post(self, request):
        user = request.user
        confirmation_code = request.data.get('confirmation_code')
        if user.confirmation_code != confirmation_code:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {'message': 'Код активации не совпадает.'}
            return response
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(status=status.HTTP_200_OK)
        invite_code = code_generator(6)
        User.objects.filter(phone_number=user.phone_number).update(
            confirmed=True, invite_code=invite_code)
        response.data = {
            'message': f'подтверждение прошло успешно - реферальный код: {invite_code}'
        }
        return response


class UserAPIView(views.APIView):

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, Verified)

    def post(self, request):
        user = request.user
        invite_code = request.data.get('invite_code')
        invite_code_user = get_object_or_404(User, invite_code=invite_code)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.invited or not User.objects.filter(invite_code=invite_code).exists():
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {
                'message': 'Вас уже пригласил другой пользователь или код приглашения не найден.'
            }
            return response
        if invite_code_user.invited_users != 'пока никого':
            invite_code_user.invited_users += f'{user.phone_number}, '
            invite_code_user.save()
        invite_code_user.invited_users = f'{user.phone_number}, '
        invite_code_user.save()
        User.objects.filter(phone_number=user.phone_number).update(
            invited=True)
        response = Response(status=status.HTTP_200_OK)
        response.data = {'message': f'Вас пригласил пользователь {invite_code_user.phone_number}'}
        return response

    def get(self, request):
        user = request.user
        response = Response(status=status.HTTP_200_OK)
        response.data = {
            'invite_code': f'Ваша реферальная ссылка - {user.invite_code}',
            'invited_users': f'Вы пригласили этих пользователей - {user.invited_users}'
        }
        return response
