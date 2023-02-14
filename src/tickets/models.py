from django.conf import settings
from django.db import models
from shared.django import TimeStampMixin


class Ticket(TimeStampMixin):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="customer_tickets",
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name="manager_tickets",
    )

    header = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return self.header
