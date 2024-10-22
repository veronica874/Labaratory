from django.db import models

# Create your models here.
class Labaratory(models.Model):
    lab_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    number_of_computers = models.IntegerField()  

    def __str__(self):
        return self.lab_name


class Lab_attendant(models.Model):
    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    attendant_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS) 
    age = models.IntegerField()  
    address = models.CharField(max_length=100)
    labaratory = models.ForeignKey(Labaratory, on_delete=models.CASCADE)

    def __str__(self):
        return self.attendant_name


class Computer(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50) 
    ram = models.CharField(max_length=10)
    lab = models.ForeignKey(Labaratory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
