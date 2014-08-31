from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def fulong(request):
    weather = {
        'wind': 'west',
        'temperature': '28',
        }
    return HttpResponse(weather['wind'])