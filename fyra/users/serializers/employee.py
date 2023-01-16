"""Employee serializers."""

# Django
from django.conf import settings
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from fyra.users.models import User

# Utilities
import jwt

# Task
from fyra.users.tasks import send_invitation_email, send_confirmation_email


class EmployeeSingUpSerializer(serializers.Serializer):
    """Employee sign up serializer.

    Handle sign up data validation and user/profile creation
    """

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    token = serializers.CharField()

    def validate(self, data):
        """Verify passwords match"""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)

        """Verify token is valid."""
        try:
            payload = jwt.decode(data['token'], settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token!')
        if payload['type'] != 'email_invitation':
            raise serializers.ValidationError('Invalid token')
        self.context['payload'] = payload
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        data.pop('token')
        data['company_name'] = self.context['payload']['company']
        user = User.objects.create_user(**data, is_verified=False, is_client=True, is_employee=True)
        send_confirmation_email.delay(user_pk=user.pk)
        return user


class NewEmployeeInvitationSerializer(serializers.Serializer):
    """"Serializer to send a email """
    email_invitation = serializers.EmailField()

    def validate_email_invitation(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists!')
        return value

    def create(self, validated_data):
        email = validated_data['email_invitation']
        user_pk = self.context['user_pk']
        send_invitation_email.delay(email, user_pk)
        return email
