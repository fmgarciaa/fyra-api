"""Orders serializers"""

# Django Rest Framework
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# Models
from fyra.orders.models.orders import Order
from fyra.orders.models.items import Items
from fyra.customers.models.customers import Customer

# Serializers
from fyra.orders.serializers.items import ItemsSerializer


class OrderSerializer(ModelSerializer):
    items = ItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['uuid', 'customer', 'payment_method', 'bank', 'delivery_date', 'is_pending', 'total_amount', 'items']

    def validate_customer(self, data):
        """
        Valid if the customer belongs to the user's company
        """
        pk = data.pk
        company = self.context['request'].user.company_name
        if not Customer.objects.filter(pk=pk, company=company):
            raise serializers.ValidationError("Customer doesn't exist!")
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['customer'] = instance.customer.name
        return representation

    def create(self, validated_data):
        """
        We need an order and its items in the same json for its update.
        """
        items_data = validated_data.pop('items')
        validated_data['company'] = self.context['request'].user.company_name
        order = Order.objects.create(**validated_data)
        for items in items_data:
            Items.objects.create(order=order, **items)
        return order

    def update(self, instance, validated_data):
        """
        We need an order and its items in the same json for its update.
        """
        items_data = validated_data.pop('items')
        instance.customer = validated_data['customer']
        instance.payment_method = validated_data['payment_method']
        instance.bank = validated_data['bank']
        instance.delivery_date = validated_data['delivery_date']
        instance.total_amount = validated_data['total_amount']
        instance.save()
        Items.objects.filter(order=instance.id).delete()
        for item in items_data:
            item['order'] = instance
            Items.objects.create(**item)

        return instance
