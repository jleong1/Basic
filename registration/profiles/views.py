from django.shortcuts import render
from .models import Profiles

def home(request):
    users = Profiles.objects.all()
    return render(request, "home.html", {'profiles':users})
