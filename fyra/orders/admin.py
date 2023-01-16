"""Products models admin."""

# Django
from django.contrib import admin

# Models
from fyra.orders.models.orders import Order
from fyra.orders.models.items import Items


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Unit model admin."""

    list_display = (
        'id',
        'uuid',
        'customer',
        'payment_method',
        'bank',
        'delivery_date',
        'is_pending',
        'total_amount',
        'company',
        'company',
        'is_removed',
        'created',
        'modified'
    )


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    """Unit model admin."""

    list_display = (
        'id',
        'uuid',
        'order',
        'product',
        'quantity',
        'sub_total',
        'is_removed',
        'created',
        'modified'
    )
