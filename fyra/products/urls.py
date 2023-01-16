"""Products urls"""

# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from fyra.products.views.units import UnitViewSet
from fyra.products.views.categories import CategoryViewSet
from fyra.products.views.products import ProductViewSet


router = DefaultRouter()

router.register(r'api/units', UnitViewSet, basename='units')
router.register(r'api/categories', CategoryViewSet, basename='categories')
router.register(r'api/products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls))
]
