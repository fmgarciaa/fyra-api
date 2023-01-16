"""Categories views"""

# Utils
from fyra.utils.views import FyraBaselViewSet

# Serializer
from fyra.products.serializers.categories import CategorySerializer


class CategoryViewSet(FyraBaselViewSet):
    """
    Inherits FyraGeneralViewSet from Utils that allow us to dont repeat code. Only
    need to change serializer_class.
    """
    serializer_class = CategorySerializer

    # Filters
    search_fields = ['name']
    filter_fields = ['name']
