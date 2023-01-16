"""Customer Model"""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utils
from fyra.utils.models import FyraAbstractModels


class Customer(FyraAbstractModels):
    """Customer model"""
    name = models.CharField(max_length=150, blank=False, null=False)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=150, blank=False, null=False)
    reference = models.CharField(max_length=150, blank=True)
    district = models.CharField(max_length=75, blank=False, null=False)
    province = models.CharField(max_length=75, blank=False, null=False)
    department = models.CharField(max_length=75, blank=True)
    company = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self) -> str:
        """Return customer name"""
        return self.name
