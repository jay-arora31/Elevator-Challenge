from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
import time
from rest_framework.response import Response





class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer




@api_view(['DELETE'])
def delete_all_data(request):
    Elevator.objects.all().delete()
    Building.objects.all().delete()
    return Response({"message": "All data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class ElevatorRequest:

    def __init__(self, number, current_floor):
        self.number = number
        self.current_floor = current_floor
        self.service_list = []
        self.direction = 0  # -1 for going down, 0 for idle, 1 for going up
        self.running = False

    def move(self):
        if not self.service_list:
            return
        target_floor = self.service_list[0]
        if target_floor > self.current_floor:
            self.direction = 1
            self.current_floor += 1
        elif target_floor < self.current_floor:
            self.direction = -1
            self.current_floor -= 1
        else:
            self.direction = 0
            self.service_list.pop(0)
            self.running = False
            print(f"Lift {self.number} door opening")
            print(f"Lift {self.number} door closing")
    
    def add_request(self, floor):
        if floor not in self.service_list:
            self.service_list.append(floor)
            self.service_list.sort(key=lambda f: abs(self.current_floor - f))
            self.direction = -1 if self.current_floor > floor else 1

    def process_service_list(self):
        ele_obj=Elevator.objects.get(number=self.number+1)
        ele_obj.running=True
        ele_obj.save()
        print("-" * 50)
        print(f"{' ' * 24} Lift - {self.number}")
        print("-" * 50)
        print("Need To Process => ", self.service_list)
        while self.service_list:
            #time.sleep(5)
            self.running = True
            while self.running:
                print(f"Lift {self.number} is at floor {self.current_floor}")
                print(f"Lift {self.number} direction is {'Going up' if self.direction == 1 else 'Going down' if self.direction == -1 else 'Idle'}")
                if self.current_floor in self.service_list:
                    print(f"Lift {self.number} stopping at floor {self.current_floor}")
                    self.service_list.remove(self.current_floor)
                    self.running = False
                else:
                    self.move()
            print(f"Lift {self.number} is currently at floor {self.current_floor}")
            print(f"Lift {self.number} running status is False")
            print(f"Lift {self.number} direction is {'Going up' if self.direction == 1 else 'Going down' if self.direction == -1 else 'Idle'}")
            print(f"Lift {self.number} door is opening")
            print(f"Lift {self.number} door is closing")
            ele_obj=Elevator.objects.get(number=self.number+1)
            ele_obj.direction=self.direction
            ele_obj.current_floor=self.current_floor
            ele_obj.running=False
            ele_obj.save()





@api_view(['POST'])
def start_lift(request):
    data_lift=Building.objects.all()
    no_of_lifts=data_lift[0].num_lifts
    no_of_floor=data_lift[0].num_floors
    lift_data=Elevator.objects.all()
    lift_pos=[]
    operational_lift=[]
    for i in lift_data:
        lift_pos.append(i.current_floor)
        if not i.maintenance:
            operational_lift.append(i.number-1)
    print("Maintainece::",operational_lift)
    request_data=JSONParser().parse(request) 
    request_each=list(request_data.get('data'))
    print(request_each)
    all_floors = []
    for i in range(no_of_floor+1):
        all_floors.append(i)
    print(all_floors)
    elevators = [ElevatorRequest(i, lift_pos[i]) for i in operational_lift]
    for floor in all_floors:
            best_elevator = None
            min_cost = float('inf')
            
            for elevator in elevators:
                cost = abs(elevator.current_floor - floor)
                if cost < min_cost:
                    min_cost = cost
                    best_elevator = elevator
            
            best_elevator.add_request(floor)
    count=0
    for i in range(len(request_each)):
        if count>no_of_lifts:
            count=0
        ele_obj=Elevator.objects.get(number=count+1)
        ele_obj.service_list=request_each[i]
        ele_obj.save()
        elevators[count].service_list = request_each[i]
        elevators[count].process_service_list()
        count+=1
    return Response({"message": "All data fetched"})


@api_view(['GET'])
def liftStatus(request):
    elevators=Elevator.objects.all()
    ele_dict={

    }
    for i in elevators:
        temp_dict={
            
            "current_floor":i.current_floor,
            "direction":i.direction,
            "lift_running_status":i.running
        }
        ele_dict["Lift  "+str(i.number)]=temp_dict
    return Response(ele_dict)





    