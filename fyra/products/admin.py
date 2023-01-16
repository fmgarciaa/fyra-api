"""Products models admin."""

# Django
from django.contrib import admin

# Models
from fyra.products.models.units import Unit
from fyra.products.models.categories import Category
from fyra.products.models.products import Product


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """Unit model admin."""

    list_display = (
        'id',
        'uuid',
        'unit',
        'abbreviation',
        'company',
        'is_removed',
        'created',
        'modified'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category model admin"""

    list_display = (
        'id',
        'uuid',
        'name',
        'company',
        'is_removed',
        'created',
        'modified'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Category model admin"""

    list_display = (
        'id',
        'uuid',
        'name',
        'category',
        'unit',
        'price',
        'company',
        'is_removed',
        'created',
        'modified'
    )
