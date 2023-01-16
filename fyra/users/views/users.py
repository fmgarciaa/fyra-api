"""Users views"""

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from fyra.users.permission import IsAccountOwner

# Models
from fyra.users.models import User


# Serializers
from fyra.users.serializers import (UserLoginSerializer,
                                    UserModelSerializer,
                                    UserSignUpSerializer,
                                    AccountVerificationSerializer,)

from fyra.users.serializers.employee import NewEmployeeInvitationSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.
    Handle sign up, login and account verification.
    """
    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAccountOwner, IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, now go use Fyra App!!'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def invitation(self, request):
        request.data['owner'] = request.user.pk
        serializer = NewEmployeeInvitationSerializer(data=request.data, context={'user_pk': request.user.pk})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Your invitation has been sent'}
        return Response(data, status=status.HTTP_200_OK)
