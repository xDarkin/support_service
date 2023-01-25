from rest_framework import serializers
from tickets.models import Ticket


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["header", "body"]


class TicketLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ["body"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
