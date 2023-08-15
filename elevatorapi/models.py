from django.db import models

# Create your models here.

class Building(models.Model):
    num_floors = models.IntegerField()
    num_lifts = models.IntegerField()
    def __str__(self):
        return f"Building (Floors: {self.floors}, Lifts: {self.num_lifts})"

class Elevator(models.Model):
    number = models.IntegerField()
    current_floor = models.IntegerField()
    service_list = models.JSONField(default=list)
    direction = models.IntegerField(default=0)
    running = models.BooleanField(default=False)

    def __str__(self):
        return f"Elevator {self.number}"