from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.permissions import RoleIsAdmin, RoleIsManager, RoleIsUser, TicketManager, TicketOwner
from tickets.serializers import TicketLightSerializer, TicketSerializer
from users.constants import Role


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    model = Ticket

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager | RoleIsUser]
        elif self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "retrieve":
            permission_classes = [TicketOwner | TicketManager | RoleIsAdmin]
        elif self.action == "update":
            permission_classes = [RoleIsAdmin | TicketManager]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin | TicketManager]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        if request.user.role == Role.ADMIN:
            queryset = self.get_queryset()
        elif request.user.role == Role.MANAGER:
            queryset = Ticket.objects.filter(manager=request.user)
        else:
            queryset = Ticket.objects.filter(customer=request.user)

        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, *args, **kwargs):
        instance: Ticket = self.get_object()
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
        instance: Ticket = self.get_object()
        context = {"request": self.request}
        serializer = TicketSerializer(instance, data=request.data, context=context, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        instance: Ticket = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
