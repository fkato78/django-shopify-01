from django.urls import path

from .views import AffiliateAPIView

app_name = "api"

urlpatterns = [
    path('', AffiliateAPIView.as_view()),
]
