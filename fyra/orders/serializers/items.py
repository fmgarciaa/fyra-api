"""Items serializers"""

# Django Rest Framework
from rest_framework import serializers

# Models
from fyra.orders.models.items import Items
from fyra.products.models.products import Product


class ItemsSerializer(serializers.ModelSerializer):
    """
    Inherits BaseSerializers from Utils that allow us to dont repeat
    code. Only need change model.
    """
    class Meta:
        model = Items
        exclude = ('is_removed', 'created', 'modified')

    def validate_product(self, data):
        """
        Validates if the product belongs to the user
        """
        pk = data.pk
        company = self.context['request'].user.company_name
        if not Product.objects.filter(pk=pk, company=company):
            raise serializers.ValidationError("Product doesn't exist!")
        return data

    def to_representation(self, instance):
        representation = {
            'uuid': instance.uuid,
            'order': instance.order.id,
            'product': instance.product.name,
            'quantity': instance.quantity,
            'price': instance.product.price,
            'sub_total': instance.sub_total,
        }
        return representation
