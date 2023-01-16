"""Stats Views"""

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from django.db.models import Sum, Count, Avg

# Serializers
from fyra.reports.serializers.stats import StatsSerializer


class StatsView(ModelViewSet):
    """
    View that allows us to display the user's company statistics.
    """
    serializer_class = StatsSerializer

    def get_queryset(self):
        company_name = self.request.user.company_name
        model = self.get_serializer().Meta.model
        queryset = model.objects.filter(company=company_name).values('company').annotate(
            total_orders=Count('id'),
            total_sell=Sum('total_amount'),
            avg_ticket=Avg('total_amount')
        )
        return queryset
