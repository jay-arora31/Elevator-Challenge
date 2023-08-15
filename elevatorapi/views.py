from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response





class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
