from django.shortcuts import render
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from collections import defaultdict

@login_required
def dashboard_home(request):

    profile = request.user.companyprofile

    if profile.role == 'consumer':

        return redirect('/')


def dashboard_home(request):

    orders = Order.objects.all()

    total_orders = orders.count()

    new_orders = orders.filter(
        status='new'
    ).count()

    completed_orders = orders.filter(
        status='completed'
    ).count()

    total_revenue = sum(
        order.total_amount
        for order in orders
    )

    monthly_orders = defaultdict(int)

    monthly_revenue = defaultdict(float)

    for order in orders:

        month = order.created_at.strftime(
            "%m.%Y"
        )

        monthly_orders[month] += 1

        monthly_revenue[month] += float(
            order.total_amount
        )

    labels = list(
        monthly_orders.keys()
    )

    orders_data = list(
        monthly_orders.values()
    )

    revenue_data = list(
        monthly_revenue.values()
    )

    return render(
        request,
        'dashboard/index.html',
        {
            'total_orders': total_orders,
            'new_orders': new_orders,
            'completed_orders': completed_orders,
            'total_revenue': total_revenue,

            'labels': labels,
            'orders_data': orders_data,
            'revenue_data': revenue_data,
        }
    )