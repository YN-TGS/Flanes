from django.shortcuts import render
from .models import Flan

# Create your views here.
def indice(request):
    flans = Flan.objects.all()
    return render(request, 'index.html', {
        'flans': flans
    })

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})



