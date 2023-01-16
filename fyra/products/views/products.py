"""Products views"""

# Django Rest Framework
from rest_framework.pagination import PageNumberPagination

# Utils
from fyra.utils.views import FyraBaselViewSet

# Serializer
from fyra.products.serializers.products import ProductSerializer


class ResultSetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 3


class ProductViewSet(FyraBaselViewSet):
    """
    Inherits FyraGeneralViewSet from Utils that allow us to dont repeat code. Only
    need to change serializer_class.
    """
    serializer_class = ProductSerializer
    pagination_class = ResultSetPagination

    # Filters
    search_fields = ('name', 'category__name',)
    filter_fields = ('name',)
