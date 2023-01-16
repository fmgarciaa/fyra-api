"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from fyra.utils.models import FyraAbstractModels


class User(FyraAbstractModels, AbstractUser):
    """User model.

    Extend form Django's Abstract User, change the username field
    to email and add some extra fields.

    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={'unique': 'A user with that email already exists.'}
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    company_name = models.CharField(
        'Company name',
        max_length=73,
        blank=False,
        null=False,
        help_text=(
            'Help easily distinguish users and perform queries. '
            "The company name provides us with a unique field to distinguish each customer's products."
        )
    )

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user. '
        )
    )

    is_owner = models.BooleanField(
        'owner company',
        default=False,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Owner are the main type of user. They have all the functions of a CRUD '
        )
    )

    is_employee = models.BooleanField(
        'employee company',
        default=False,
        help_text=(
            'Help easily distinguish employee and perform queries. '
            'Employees can only create, read and update'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address. '
    )

    def __str__(self) -> str:
        """Return username"""
        return self.username

    def get_short_name(self) -> str:
        """Return username."""
        return self.username
