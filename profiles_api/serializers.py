from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
