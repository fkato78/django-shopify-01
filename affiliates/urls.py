from django.urls import path

from .views import AffiliateList, login


app_name = "affiliates"

urlpatterns = [
    path('affiliate/', AffiliateList.as_view(), name="list"),
    path('affiliate-login/', login, name='affiliate_login'),
]
