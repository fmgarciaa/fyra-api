"""Orders Model"""

# Django
from django.db import models

# Models
from fyra.customers.models.customers import Customer

# Utils
from fyra.utils.models import FyraAbstractModels


class Order(FyraAbstractModels):
    """Order model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=75, blank=True)
    bank = models.CharField(max_length=75, blank=True)
    delivery_date = models.DateField(blank=False, null=False)
    is_pending = models.BooleanField(default=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=8, blank=False)
    company = models.CharField(max_length=75, blank=False, null=False)

    def __str__(self):
        """Return customer"""
        return str(self.customer)
