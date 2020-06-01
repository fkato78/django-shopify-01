from django.contrib import admin

from .models import Affiliate


@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "code")
    list_filter = ("name", "email",)
    search_fields = ("name", "email")
    ordering = ("name", "code")
