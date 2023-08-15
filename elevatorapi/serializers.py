from .models import Building, Elevator
from rest_framework import serializers

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'