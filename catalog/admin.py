from django.contrib import admin

from .models import (
    Category,
    Product
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price_per_unit',
        'stock',
        'available'
    )

    list_filter = (
        'category',
        'available'
    )

    search_fields = (
        'name',
    )


admin.site.register(Category)