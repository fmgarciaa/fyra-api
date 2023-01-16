"""Units views"""

# Utils
from fyra.utils.views import FyraBaselViewSet

# Serializer
from fyra.products.serializers.units import UnitSerializer


class UnitViewSet(FyraBaselViewSet):
    """
    Inherits FyraGeneralViewSet from Utils that allow us to dont repeat code. Only
    need to change serializer_class.
    """
    serializer_class = UnitSerializer

    # Filters
    # Filters
    search_fields = ['unit', 'abbreviation']
    filter_fields = ['unit']
