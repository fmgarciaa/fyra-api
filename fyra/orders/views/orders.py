"""Orders views"""

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

# Serializer
from fyra.orders.serializers.orders import OrderSerializer

# Permissions
from fyra.users.permission import IsOwner
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ResultSetPagination(PageNumberPagination):
    """
    Custom pagination class
    """
    page_size = 100
    max_page_size = 100


class OrderViewSet(ModelViewSet):
    """
    Inherits FyraGeneralViewSet from Utils that allow us to dont repeat code. Only
    need to change serializer_class.
    """
    serializer_class = OrderSerializer
    lookup_field = 'uuid'
    pagination_class = ResultSetPagination

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('customer__name', 'delivery_date')
    ordering = ('-modified',)
    filter_fields = ('is_pending',)

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action == 'destroy':
            permissions.append(IsOwner)
        return [p() for p in permissions]

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_removed=False, company=self.request.user.company_name)

    def destroy(self, request, uuid=None):
        order = self.get_queryset().filter(uuid=uuid).first()
        if order:
            order.is_removed = True
            order.save()
            return Response({'message': 'Successfully deleted!'}, status=status.HTTP_200_OK)
