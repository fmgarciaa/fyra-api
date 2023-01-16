"""Orders URLs"""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from fyra.reports.views.stats import StatsView

router = DefaultRouter()
router.register(r'api/stats', StatsView, basename='stats')

urlpatterns = [
    path('', include(router.urls))
]
