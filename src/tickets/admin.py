from django.contrib import admin
from shared.django import TimeStampReadonlyAdmin
from tickets.models import Ticket


@admin.register(Ticket)
class TicketAdmin(TimeStampReadonlyAdmin):
    list_display = ["header", "id", "customer", "manager"]
    list_filter = ["customer", "manager"]
    search_fields = ["header"]
