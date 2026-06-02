from django.urls import path

from .views import *

urlpatterns = [

    path(
        'cart/',
        cart_view,
        name='cart'
    ),

    path(
        'add/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'remove/<int:product_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'create/',
        create_order,
        name='create_order'
    ),

    path(
        'my/',
        my_orders,
        name='my_orders'
    ),

    path(
        'detail/<int:order_id>/',
        order_detail,
        name='order_detail'
    ),

    path(
        'export-excel/',
        export_orders_excel,
        name='export_orders_excel'
    ),

    path(
        'manage/',
        manage_orders,
        name='manage_orders'
    ),

    path(
        'status/<int:order_id>/<str:status>/',
        change_order_status,
        name='change_order_status'
    ),
]