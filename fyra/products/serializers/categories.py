"""Categories serializers"""

# Utils
from fyra.utils.serializers import FyraBaseSerializer

# Models
from fyra.products.models.categories import Category


class CategorySerializer(FyraBaseSerializer):
    """
    Inherits BaseSerializers from Utils that allow us to dont repeat
    code. Only need change model.
    """
    class Meta(FyraBaseSerializer.Meta):
        model = Category

    def to_representation(self, instance):
        view_api = {
            'uuid': instance.uuid,
            'name': instance.name
        }
        return view_api
