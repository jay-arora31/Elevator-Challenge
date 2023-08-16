#importing Libraries

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import time




#class for performing crud operation for building model
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    

#class for performing crud operation for elevator model
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
        self.number = number+1
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
        ele_obj=Elevator.objects.get(number=self.number)
        ele_obj.running=True
        ele_obj.save()
        print("-" * 50)
        print(f"{' ' * 24} Lift - {self.number}")
        print("-" * 50)
        print("Need To Process => ", self.service_list)
        while self.service_list:
            time.sleep(3)
            self.running = True
            while self.running:
                print(f"Lift {self.number} direction is {'Going up' if self.direction == 1 else 'Going down' if self.direction == -1 else 'Idle'}")
                print(f"Lift {self.number} is at floor {self.current_floor}")
                if self.current_floor in self.service_list:
                    print(f"Lift {self.number} stopping at floor {self.current_floor}")
                    self.service_list.remove(self.current_floor)
                    self.running = False
                else:
                    self.move()
            #print(f"Lift {self.number} is currently at floor {self.current_floor}")
            #print(f"Lift {self.number} direction is {'Going up' if self.direction == 1 else 'Going down' if self.direction == -1 else 'Idle'}")
            print(f"Lift {self.number} running status is False")
            print(f"Lift {self.number} door is opening")
            print(f"Lift {self.number} door is closing")
            ele_obj=Elevator.objects.get(number=self.number)
            ele_obj.direction=self.direction
            ele_obj.current_floor=self.current_floor
            ele_obj.running=False
            ele_obj.save()



def checkServiceRequest(lists):
    building=Building.objects.all()
    return all(building[0].min_floor <= number <= building[0].max_floors for sublist in lists for number in sublist)


@api_view(['POST'])
def start_lift(request):
    lift_pos=[]
    operational_lift=[]
    all_floors = []
    data_lift=Building.objects.all()
    lift_data=Elevator.objects.all()
    if data_lift:
        #getting the request data service list
        request_data=JSONParser().parse(request) 

        no_of_lifts=data_lift[0].num_lifts
        no_of_floor=data_lift[0].max_floors
        #converting servicelist dict into simple 2dlist
        request_each=list(request_data.get('data'))
        # filter only operational lift  appending their  current floor in lift_pos list
        for i in lift_data:
            lift_pos.append(i.current_floor)
            if not i.maintenance:
                operational_lift.append(i.number-1)
        check_service=checkServiceRequest(request_each)
        if check_service:
                if len(request_each)<=len(operational_lift):  
                    for i in range(no_of_floor+1):
                        all_floors.append(i)
                    elevators = [ElevatorRequest(i, lift_pos[i]) for i in operational_lift]
                    for floor in all_floors:
                            best_elevator = None
                            min_cost = float('inf')
                            for elevator in elevators:
                                cost = abs(elevator.current_floor - floor)
                                # finding optimal cost value
                                if cost < min_cost:
                                    min_cost = cost
                                    best_elevator = elevator
                            best_elevator.add_request(floor)
                    count=0

                    for i in range(len(request_each)):
                        ele_obj=Elevator.objects.get(number=count+1)
                        ele_obj.service_list=request_each[i]
                        ele_obj.save()
                        elevators[count].service_list = request_each[i]
                        elevators[count].process_service_list()
                        count+=1
                        elevators_data=Elevator.objects.all()
                        ele_dict={
                        }
                        for i in elevators_data:
                            temp_dict={
                                "current_floor":i.current_floor,
                                "direction":i.direction,
                                "lift_running_status":i.running
                            }
                            ele_dict["Lift  "+str(i.number)]=temp_dict
                        return Response(ele_dict)
                    return Response({"message": "All data fetched"})
                else:
                    return Response({"message": "Number of service list should equal or less than of number of operational lift"})
        else:
            return Response({"message": "Service List value should in range of "+str(data_lift[0].min_floor)+" and "+ str(data_lift[0].max_floors)})
    else:
        print("I am here")
        return Response({"message": "first insert building values minimum-floor, maximum-floor, number of lift"})



# function for getting lift status
@api_view(['GET'])
def liftStatus(request):
    elevators=Elevator.objects.all()
    ele_dict={}
    for i in elevators:
        temp_dict={
            "current_floor":i.current_floor,
            "direction":i.direction,
            "lift_running_status":i.running
        }
        ele_dict["Lift  "+str(i.number)]=temp_dict
    return Response(ele_dict)





    