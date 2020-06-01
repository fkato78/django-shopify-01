from rest_framework import generics
from affiliates.models import Affiliate
from .serializers import AffiliateSerializer


class AffiliateAPIView(generics.ListAPIView):
    queryset =  Affiliate.objects.all()
    serializer_class = AffiliateSerializer