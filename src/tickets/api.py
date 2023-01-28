from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def list(self, request, *args, **kwargs):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, *args, **kwargs):
        instance = Ticket.objects.get(id=kwargs["pk"])
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request, *args, **kwargs):
        context = {"request": self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = Ticket.objects.get(id=kwargs["pk"])
        context = {"request": self.request}
        serializer = TicketSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        instance = Ticket.objects.get(id=kwargs["pk"])
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
