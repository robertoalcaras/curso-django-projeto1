from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return HttpResponse('HOME 1')
    return render(request, 'recipes/home.html', context={
        'name': 'Roberto Alcaras',
    })

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(request):
    return HttpResponse('Sobre novo')
