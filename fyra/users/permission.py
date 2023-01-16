"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj


class IsOwner(BasePermission):
    """
    Object-level permission to allow owner a complete CRUD
    """
    message = 'No access. 0nly owners can delete a objects'

    def has_permission(self, request, view):
        """Check user is owner"""
        return request.user.is_owner
