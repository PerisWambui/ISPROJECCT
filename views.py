from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    # return HttpResponse('Hello, I am Peris')
    return render(request, 'home.html')
