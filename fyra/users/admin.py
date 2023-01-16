"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from fyra.users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'company_name', 'is_staff',
                    'is_client', 'is_verified', 'is_owner', 'is_employee')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
