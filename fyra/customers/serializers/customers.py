"""Customers serializers"""
# Django REST Framework
from rest_framework import serializers

# Utils
from fyra.utils.serializers import FyraBaseSerializer

# Models
from fyra.customers.models.customers import Customer


class CustomerSerializer(FyraBaseSerializer):
    """
    Inherits FyraBaseSerializers from Utils that allow us to dont repeat
    code. Only need change model.
    """
    class Meta(FyraBaseSerializer.Meta):
        model = Customer

    def to_representation(self, instance):
        view_api = {
            'uuid': instance.uuid,
            'name': instance.name,
            'phone': instance.phone,
            'email': instance.email,
            'address': instance.address,
            'reference': instance.reference,
            'district': instance.district,
            'province': instance.province,
            'department': instance.department,
        }
        return view_api

    def validate_name(self, data):
        company = self.context['request'].user.company_name
        name = data
        if Customer.objects.filter(name=name, company=company).exists():
            raise serializers.ValidationError('There is already a customer with that name!')
        return data
