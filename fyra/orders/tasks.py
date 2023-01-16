"""Task to Celery"""
# Django
from django.utils import timezone

# Models
from fyra.orders.models.orders import Order

# Celery
from config import celery_app


@celery_app.task(name='disable_finished_orders')
def closed_orders():
    """Change status from is_pending on Order that have finished"""
    now = timezone.now()

    # Update orders that have already finished
    closed_orders = Order.objects.filter(delivery_date__lt=now, is_pending=True)
    closed_orders.update(is_pending=False)
