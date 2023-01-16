"""Users URLs"""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as user_views
from .views import employee as employee_views

router = DefaultRouter()
router.register(r'api/users', user_views.UserViewSet, basename='users')
router.register(r'api/employee', employee_views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls))
]
