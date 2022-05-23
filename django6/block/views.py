from django.shortcuts import render
from .models import Home

def home(request):
    home = Home.objects.all()
    context = {
        "homes": home
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')