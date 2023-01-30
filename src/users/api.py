from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from users.serializers import UserRegistrationSerializer, UserSerializer
from users.permissions import RoleIsAdmin, UserOwner
from rest_framework.permissions import AllowAny

User = get_user_model()


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [AllowAny]
        elif self.action == "retrieve":
            permission_classes = [UserOwner | RoleIsAdmin]
        elif self.action == "update":
            permission_classes = [RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, *args, **kwargs):
        instance: User = self.get_object()
        serializer = UserSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request, *args, **kwargs):
        context = {"request": self.request}
        serializer = UserRegistrationSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance: User = self.get_object()
        context = {"request": self.request}
        serializer = UserSerializer(instance, data=request.data, context=context, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        instance: User = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
