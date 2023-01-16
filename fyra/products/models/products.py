"""Products Model"""

# Django
from django.db import models

# products.models
from fyra.products.models.categories import Category
from fyra.products.models.units import Unit

# Utils
from fyra.utils.models import FyraAbstractModels


class Product(FyraAbstractModels):
    """Product model"""
    name = models.CharField(max_length=150, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, blank=False, null=False, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    company = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        """Return product name."""
        return self.name
