"""Items Model"""

# Django
from django.db import models

# Models
from fyra.orders.models.orders import Order
from fyra.products.models.products import Product

# Utils
from fyra.utils.models import FyraAbstractModels


class Items(FyraAbstractModels):
    """Order model"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    sub_total = models.DecimalField(decimal_places=2, max_digits=8, blank=False)

    def __str__(self):
        """Return customer"""
        return str(self.product)
