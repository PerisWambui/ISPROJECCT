from django.shortcuts import render
from django.http import HttpResponse

from .models import Hospital, Insurance, Location, Doctor

def home (request):
    # return HttpResponse('Hello, I am Peris')
    return render(request, 'home.html')


def location(request):
    locations = Location.objects.all()

    # Insurance.objects.all().delete()
    # print()
    # print('Insurance table truncated successfully!')
    # print()

    context = {
        'locations': locations,
    }
    return render(request, 'location.html', context)


def hospitals_in(request, location_id):
    hospitals = Hospital.objects.filter(location_id=location_id)
    selected_location = Location.objects.get(id=location_id)
    
    context = {
        'hospitals': hospitals,
        'selected_location': selected_location,
    }
    return render(request, 'hospitals.html', context)


def hospital(request, hospital_id):
    hospital = Hospital.objects.get(id=hospital_id)
    context = {
        'hospital': hospital
    }
    return render(request, 'hospital.html', context)


def doctors(request, hospital_id):

    doctors = Doctor.objects.filter(hospital_id = hospital_id)
    selected_hospital = Hospital.objects.get(id = hospital_id)
    context ={
        'doctors' : doctors,
        'selected_hospital' : selected_hospital,
    }
    return render(request,'doctors.html', context)

    