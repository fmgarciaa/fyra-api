"""Customers urls"""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from fyra.customers.views.customers import CustomerViewSet


router = DefaultRouter()

router.register(r'api/customers', CustomerViewSet, basename='customers')


urlpatterns = [
    path('', include(router.urls))
]
