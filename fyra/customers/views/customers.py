"""Customers views"""

# Utils
from fyra.utils.views import FyraBaselViewSet

# Serializer
from fyra.customers.serializers.customers import CustomerSerializer


class CustomerViewSet(FyraBaselViewSet):
    """
    Inherits FyraGeneralViewSet from Utils that allow us to dont repeat code. Only
    need to change serializer_class.
    """
    serializer_class = CustomerSerializer

    # Filters
    search_fields = ('name', 'district',)
    filter_fields = ('name',)
