from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def indice(request):
    flans = Flan.objects.all()
    return render(request, 'index.html', {
        'flans': flans
    })

def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)

    
    return render(request, 'welcome.html', {
        'private_flans': private_flans

    })

def contacto(request):

    if request.method == 'POST':

        form = ContactFormModelForm(request.POST)
        if form.is_valid():

            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:

            form = ContactFormModelForm()
        
    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'success.html',{}) 