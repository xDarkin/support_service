from django.conf import settings
from django.db import models
from shared.django import TimeStampMixin
from tickets.models import Ticket


class Comment(TimeStampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="comments",
    )
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    body = models.TextField()
