from django.db.models import Sum, Count, Avg

from fyra.orders.models.orders import Order
from dataclasses import dataclass


@dataclass
class ReportStats:
    company = None
    total: int


def stats_report():
    queryset = Order.objects.values('company').annotate(
        total_order=Count('id'),
        total_amount_sum=Sum('total_amount'),
        total_amount_avg=Avg('total_amount')
    )
    return queryset
