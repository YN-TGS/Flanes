from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm


# Create your views here.
def indice(request):
    flans = Flan.objects.all()
    return render(request, 'index.html', {
        'flans': flans
    })

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)

    
    return render(request, 'welcome.html', {
        'private_flans': private_flans

    })

def contacto(request):
    print("Afuera del IF")
    if request.method == 'POST':
        print("Entro al IF")
        form = ContactFormForm(request.POST)
        if form.is_valid():
            print("Formulario Valido")
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
            print("FOrmulario No Valido")
            form = ContactFormForm()
        
    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'success.html',{}) 