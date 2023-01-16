"""Products models admin."""

# Django
from django.contrib import admin

# Models
from fyra.customers.models.customers import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Unit model admin."""

    list_display = (
        'id',
        'uuid',
        'name',
        'phone',
        'email',
        'address',
        'reference',
        'district',
        'province',
        'department',
        'company',
        'is_removed',
        'created',
        'modified'
    )
