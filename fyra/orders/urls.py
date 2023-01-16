"""Orders urls"""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from fyra.orders.views.orders import OrderViewSet

router = DefaultRouter()

router.register(r'api/orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls))
]
