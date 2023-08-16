# Backend Problem Statement : Elevator System

## Demo Video
https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/5cc2f250-14a1-4aa1-8041-ec67289f0c0d

### Solution Overview
The elevator logic in the provided solution involves an object-oriented approach to simulate the behavior of multiple elevators. Each elevator is represented by an instance of the ElevatorRequest class. When a request for elevator service is received, the algorithm determines the best-suited elevator for the task based on a cost-minimization strategy. The cost is calculated as the absolute difference between the current floor of the elevator and the requested floor. The elevator with the lowest cost is assigned the request. Once assigned, the elevator processes its service list in a continuous loop. It moves towards the requested floor, opens its doors upon reaching the floor, and continues processing further requests. This simulates the movement, stopping, and operation of elevators in a building. The elevator logic ensures efficient handling of service requests while considering elevator positions and directions, making the system responsive to user requests and maintaining optimal efficiency in elevator operations.


# Elevator System Project Structure

```plaintext
elevatormain/
│
├── elevatorapi/
│   ├── migrations/
│   ├── admin.py
│   ├── app.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── elevatormain/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.pywsgi
│   ├── wsgi.py
│  
├── manage.py
├── requirements.txt
├── README.md

```
<h2>Setup :</h2>

Clone the repository to your local machine:
```sh
$ git clone https://github.com/jay-arora31/Elevator-Challenge.git
$ cd Elevator-Challenge
```

Install the required dependencies:
```sh
$ pip install -r requirements.txt


```

Apply database migrations:
```sh
$ python manage.py migrate


```

Start the development server:
```sh
$ python manage.py runserver


```

# Elevator System API Contracts

## Get All Buildings or Create a New Building
#### note: add only one building data
- **Endpoint**: `api/building/`
- **Method**: GET (Get all buildings), POST (Create a new building)
- **Requests Body (POST)**: JSON object containing building details (min_floor, max_floor, num_lifts)
- **Example**:
```sh
    {
    'min_floor':0,
    'max_floor': 20,
    'num_lifts':5
    }


```
- **Response (GET)**:
- **Status**: 200 OK
- **Content**: List of buildings with their details


## Get, Update, or Delete a Building
- **Endpoint**: `/building/<building_id>/`
- **Method**: GET (Get building details), PUT (Update building details), DELETE (Delete a building)
- **Response (GET)**:
  - **Status**: 200 OK
  - **Content**: Building details
- **Request Body (PUT)**: JSON object containing updated building details
- **Response (PUT)**:
  - **Status**: 200 OK
  - **Content**: Updated building details
- **Response (DELETE)**:
  - **Status**: 204 No Content


## Get All Elevators or Create a New Elevator
- **Endpoint**: `/elevator/`
- **Method**: GET (Get all elevators), POST (Create a new elevator)
- **Request Body (POST)**: JSON object containing elevator details (number, current_floor, maintenance)
- **Response (GET)**:
  - **Status**: 200 OK
  - **Content**: List of elevators with their details
  
## Get, Update, or Delete an Elevator
- **Endpoint**: `/elevator/<elevator_id>/`
- **Method**: GET (Get elevator details), PUT (Update elevator details), DELETE (Delete an elevator)
- **Response (GET)**:
  - **Status**: 200 OK
  - **Content**: Elevator details
- **Request Body (PUT)**: JSON object containing updated elevator details
- **Response (PUT)**:
  - **Status**: 200 OK
  - **Content**: Updated elevator details
- **Response (DELETE)**:
  - **Status**: 204 No Content
 
  
## Delete All Data
- **Endpoint**: `/deleteAllData/`
- **Method**: DELETE
- **Response**:
  - **Status**: 204 No Content

## Request Lift 
- **Endpoint**: `/requestLift/`
- **Method**: POST
- **Request Body**: JSON object containing service_list (list of floors to be served)
- **Example**:
```sh
    {
      "service_list":[[4,3,9],[6,0,4]]
    }
```
- **Response**:
  - **Status**: 200 OK
  - **Content**: Elevator statuses after processing the service requests
  
## Get Elevator Status
- **Endpoint**: `/liftStatus/`
- **Method**: GET
- **Response**:
  - **Status**: 200 OK
  - **Content**: Current statuses of all elevators



# Output

### Inserting Building value min_floor, max_floor, num_lifts

![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/a0bad869-3501-4b00-9413-e185de6fc8b2)

### After inserting the Building models value number of elevator create automaticlly based on Building(num_lifts)
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/e4016ebe-9178-4074-8c4b-e8c276653c6c)

## Default position of all elevators is currently 0
## Changing  elevator 1 maintenance true 
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/14ed3509-a2b2-4077-b4aa-cabffba577fe)


## Changing elevator2 default position to 5
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/0f6b10f2-8d23-4782-a851-c4d9dc66f9e7)


## Requesting elevator Service
#### elevator 1  is in maintenance
#### elevator 2
#####    
        {
       "service_list": [ [1, 9, 8], [4, 0, 5]]
        }
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/f7eacf76-59de-4759-831c-0c7d3afd13e8)
#### elevator 3
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/ca12fade-6de3-456e-9388-f166fca97b50)

# All Elevators Status
![image](https://github.com/jay-arora31/Elevator-Challenge/assets/68243425/c748a1f7-2eb2-452b-90a3-1611bbcda4b0)
