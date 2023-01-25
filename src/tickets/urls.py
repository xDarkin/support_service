from django.http import JsonResponse
from django.urls import path
from rest_framework.generics import CreateAPIView, ListAPIView
from tickets.models import Ticket
from tickets.serializers import TicketCreateSerializer, TicketLightSerializer, TicketSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLightSerializer


def get_ticket(request, id_: int) -> JsonResponse:
    ticket: Ticket = Ticket.objects.get(id=id_)
    serializer = TicketSerializer(ticket)
    return JsonResponse(serializer.data)


class TicketCreateAPI(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


urlpatterns = [
    path("list/", TicketsGet.as_view()),
    path("create/", TicketCreateAPI.as_view()),
    path("<int:id_>", get_ticket),
]
