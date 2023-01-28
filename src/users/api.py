from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import status

# from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from users.serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


class UserAPISet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    def retrieve(self, request, *args, **kwargs):
        instance = User.objects.get(id=kwargs["pk"])
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
        instance = User.objects.get(id=kwargs["pk"])
        context = {"request": self.request}
        serializer = UserSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        instance = User.objects.get(id=kwargs["pk"])
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
