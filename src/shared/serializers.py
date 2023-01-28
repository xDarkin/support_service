from rest_framework import serializers


class ResponseSerializer(serializers.Serializer):
    result = serializers.DictField()


class ResponseMultiSerializer(serializers.Serializer):
    results = serializers.ListField()
