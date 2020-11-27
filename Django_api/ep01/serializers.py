from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 40)
    roll = serializers.CharField(max_length = 10)
    city = serializers.CharField(max_length = 20)