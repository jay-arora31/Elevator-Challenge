from django.db import models

# Create your models here.

class Elevator(models.Model):
    number = models.IntegerField(default=1000,null=True,blank=True)
    current_floor = models.IntegerField(default=0)
    service_list = models.JSONField(default=list,null=True,blank=True)
    direction = models.IntegerField(default=0,null=True,blank=True)
    running = models.BooleanField(default=False)
    maintenance=models.BooleanField(default=False)

    def __str__(self):
        return f"Elevator {self.number}"
class Building(models.Model):
    num_floors = models.IntegerField()
    num_lifts = models.IntegerField()
    def __str__(self):
        return f"Building (Floors: {self.floors}, Lifts: {self.num_lifts})"
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super(Building, self).save(*args, **kwargs)
        if is_new:
            for elevator_number in range(1, self.num_lifts + 1):
                Elevator.objects.create(number=elevator_number)
