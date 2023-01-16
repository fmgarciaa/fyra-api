"""Products serializers"""

# Utils
from fyra.utils.serializers import FyraBaseSerializer

# Models
from fyra.products.models.products import Product
from fyra.products.models.categories import Category
from fyra.products.models.units import Unit

# Django Rest Framework
from rest_framework import serializers


class ProductSerializer(FyraBaseSerializer):
    """
    Inherits BaseSerializers from Utils that allow us to dont repeat
    code. Only need change model.
    """
    class Meta(FyraBaseSerializer.Meta):
        model = Product

    def to_representation(self, instance):
        view_api = {
            'uuid': instance.uuid,
            'name': instance.name,
            'category': instance.category.name,
            'unit': instance.unit.abbreviation,
            'price': instance.price
        }
        return view_api

    def validate_category(self, data):
        """
        Valid if the category belongs to the user's company
        """
        company = self.context['request'].user.company_name
        pk = data.pk
        if not Category.objects.filter(pk=pk, company=company).exists():
            raise serializers.ValidationError("Category doesn't exist")
        return data

    def validate_unit(self, data):
        """
        Valid if the unit belongs to the user's company
        """
        company = self.context['request'].user.company_name
        pk = data.pk
        if not Unit.objects.filter(pk=pk, company=company).exists():
            raise serializers.ValidationError("Category doesn't exist")
        return data
