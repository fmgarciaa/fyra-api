"""Units serializers"""

# Utils
from fyra.utils.serializers import FyraBaseSerializer

# Models
from fyra.products.models.units import Unit


class UnitSerializer(FyraBaseSerializer):
    """
    Inherits BaseSerializers from Utils that allow us to dont repeat
    code. Only need change model.
    """
    class Meta(FyraBaseSerializer.Meta):
        model = Unit

    def to_representation(self, instance):
        view_api = {
            'uuid': instance.uuid,
            'unit': instance.unit,
            'abbreviation': instance.abbreviation
        }
        return view_api
