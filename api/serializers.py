# api/serializers.py
from rest_framework import serializers

from affiliates.models import Affiliate


class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = ('name', 'email', 'code')
