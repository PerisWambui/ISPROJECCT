from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE, SET_NULL
#Admin
# password: userPa$$

class HospitalService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=50)

    def __str__(self):
        return f'Location: {self.name}, Postal address address: {self.postal_address}'


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    services = models.ManyToManyField(HospitalService)

    def __str__(self):
        return f'Hospital: {self.name}, location: {self.location.name}'


class Insurance(models.Model):
    name = models.CharField(max_length=200) 
    hospital = models.ForeignKey(Hospital, on_delete=CASCADE) 

    def __str__(self):
        return f'Insurance: {self.name}, hospital: {self.hospital.name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200) 
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, blank=True, null=True) 
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Doctor: {self.first_name} {self.last_name}, hospital: {self.hospital.name}, specialization: {self.specialization}'


   
