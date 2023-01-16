"""Units models"""

# Django
from django.db import models

# Utils
from fyra.utils.models import FyraAbstractModels


class Unit(FyraAbstractModels):
    """Unit model"""
    unit = models.CharField(max_length=73, blank=False, null=False)
    abbreviation = models.CharField(max_length=15, blank=False, null=False)
    company = models.CharField(max_length=113, blank=False, null=False)

    def __str__(self):
        """Return unit name."""
        return self.unit
