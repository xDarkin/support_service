from rest_framework import serializers
from tickets.models import Ticket


class TicketLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ["body", "created_at", "updated_at"]


class TicketSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ticket
        fields = ["id", "customer", "header", "body"]
