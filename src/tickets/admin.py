from django.contrib import admin
from shared.django import TimeStampReadonlyAdmin
from tickets.models import Ticket


@admin.register(Ticket)
class TicketAdmin(TimeStampReadonlyAdmin):
    pass
