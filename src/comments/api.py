from comments.models import Comment
from comments.serializers import CommentSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from users.constants import Role


class CommentAPISet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    model = Comment
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def list(self, request, *args, **kwargs):

        if request.user.role == Role.ADMIN:
            tickets = Ticket.objects.all()
        elif request.user.role == Role.MANAGER:
            tickets = Ticket.objects.filter(manager=self.request.user)
        else:
            tickets = Ticket.objects.filter(customer=self.request.user)

        ticket: Ticket = get_object_or_404(tickets, id=kwargs[self.lookup_field])
        queryset = ticket.comments.order_by("-created_at")
        # queryset = Comment.objects.filter(ticket_id=kwargs[self.lookup_field])
        serializer = CommentSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def create(self, request, *args, **kwargs):
        context = {"request": self.request}
        serializer = CommentSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)


# The OR SQL processing
# from django.db.models import Q
# tickets = Ticket.objects.filter(
#     Q(manager=self.request.user) | Q(customer=self.request.user)
# )
