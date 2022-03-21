from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import User


class SignupSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = ('phone_number', )

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class ValidateSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(
        required=True,
    )

    class Meta:
        model = User
        fields = ('confirmation_code', )

    def validate(self, attrs):
        confirmation_code = attrs.get('confirmation_code')
        user = get_object_or_404(User, confirmation_code=confirmation_code)
        if user.confirmation_code == confirmation_code:
            return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('invite_code', )

    def validate(self, attrs):
        return super().validate(attrs)
