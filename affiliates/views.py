from django.shortcuts import render
from django.views.generic import ListView

from .models import Affiliate


class AffiliateList(ListView):
    model = Affiliate
    template_name = "affiliates/index.html"
    context_object_name = "affiliates"


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

    return render(request, "auth/login.html", {'affiliate': 'fares'})