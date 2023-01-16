"""Base serializers"""

# Django Rest Framework
from rest_framework import serializers


class FyraBaseSerializer(serializers.ModelSerializer):
    """FyraBaseSerialize.
    This BaseSerializer allow us inherit it to dont repeat same code in each serializer.
    """

    class Meta:
        model = None
        exclude = ('is_removed', 'created', 'modified')
