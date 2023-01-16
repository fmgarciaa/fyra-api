"""Categories Models"""

# Django
from django.db import models

# Utils
from fyra.utils.models import FyraAbstractModels


class Category(FyraAbstractModels):
    """Category model"""
    name = models.CharField(max_length=75, blank=False, null=False)
    company = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        """Return category name."""
        return self.name
