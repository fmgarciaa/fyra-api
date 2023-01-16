"""Statistics serializers"""

# Django Rest Framework
from rest_framework import serializers

# Models
from fyra.orders.models.orders import Order


class StatsSerializer(serializers.ModelSerializer):
    """
    Serializer that allows us to generate order statistics such as:
        total_order: total orders of the company.
        total_sell: total sells of the company.
        avg_ticket: Orders Average ticket of the company.
    """
    total_orders = serializers.IntegerField()
    total_sell = serializers.DecimalField(max_digits=10, decimal_places=2)
    avg_ticket = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Order
        fields = ('total_orders', 'total_sell', 'avg_ticket')
