from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 40)
    roll = serializers.CharField(max_length = 10)
    city = serializers.CharField(max_length = 20)

    # Create Function
    def create(self, validated_data):
        return Students.objects.create(**validated_data)