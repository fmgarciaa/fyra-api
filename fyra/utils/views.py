"""Views utils"""

# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Permissions
from fyra.users.permission import IsOwner

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class FyraBaselViewSet(viewsets.ModelViewSet):
    """GeneralViewSet.
    It allow us manage a complete CRUD
    """
    serializer_class = None
    lookup_field = 'uuid'

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = None
    ordering = ('modified',)
    filter_fields = None

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action == 'destroy':
            permissions.append(IsOwner)
        return [p() for p in permissions]

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_removed=False, company=self.request.user.company_name)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['company'] = request.user.company_name
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, uuid=None):
        obj = self.get_queryset().filter(uuid=uuid).first()
        if obj:
            obj.is_removed = True
            obj.save()
            return Response({'message': 'Successfully deleted!'}, status=status.HTTP_200_OK)
