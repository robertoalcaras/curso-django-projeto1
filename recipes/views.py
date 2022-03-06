from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse('HOME 1')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Roberto Alcaras',
    })


