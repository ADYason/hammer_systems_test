from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex='^.{11}$', message='Length has to be 11', code='nomatch'
            )
        ],
    )
    confirmation_code = models.CharField(
        max_length=4
    )
    invite_code = models.CharField(
        max_length=6
    )
    invited_users = models.TextField(
        default='пока никого'
    )
    username = models.CharField(
        max_length=150,
        unique=False,
        default=''
    )
    confirmed = models.BooleanField(default=False)
    invited = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['phone_number']
