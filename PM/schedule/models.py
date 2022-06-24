from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user_id = models.IntegerField()

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    employer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    position = models.CharField(max_length=50)
    etat = (
        ("F", 'Full-Time'),
        ("H", 'Half-Time'),
        ("Q", '3/4 Time')
    )
    work_time = models.CharField(max_length=1, choices=etat)

    def __str__(self):
    	return self.name


class Work_day(models.Model):
    employer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()
    hours = (
        ("A", '9-17'),
        ("B", '11-19'),
        ("C", '13-21'),
        ("G", '9-21')
    )
    time = models.CharField(max_length=1, choices=hours)
    worked_hours = models.IntegerField()
    def __str__(self):
    	return f'{self.day} {self.employee}'

class Vacation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'{self.employee} {self.start_date} {self.end_date}'

class Free_days(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
    	return f'{self.employee} {self.date}'