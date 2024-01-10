from django.contrib import admin

from mobilefetcher.models import InvestigatedAccount
from mobilefetcher.models import FetchingAccount

@admin.register(InvestigatedAccount)
class InvestigatedAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(FetchingAccount)
class FetchingAccountAdmin(admin.ModelAdmin):
    pass
