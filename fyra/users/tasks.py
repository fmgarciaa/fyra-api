"""Tasks to Celery"""

# Django
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

# Models
from fyra.users.models.users import User

# Utilities
import jwt
from datetime import timedelta

from config import celery_app


@celery_app.task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to give user."""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Welcome @{}! Verify your account to start using Fyra App'.format(user.username)
    from_email = 'Fyra <noreply@fyra.com>'
    content = render_to_string(
        'email/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, 'text/html')
    msg.send()


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


@celery_app.task(name='send_invitation_email', max_retries=3)
def send_invitation_email(email, user_pk):
    """Send invitation link to new employee."""
    user = User.objects.get(pk=user_pk)
    email_token = gen_invitation_token(user)
    subject = 'Fyra App - Email invitation to join {} company '.format(user.company_name)
    from_email = 'Fyra <noreply@fyra.com>'
    content = render_to_string(
        'email/users/email_invitation.html',
        {'token': email_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [email])
    msg.attach_alternative(content, 'text/html')
    msg.send()


def gen_invitation_token(user):
    """Create JWT token that the new employee can use to create your account"""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'company': user.company_name,
        'exp': int(exp_date.timestamp()),
        'type': 'email_invitation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token
