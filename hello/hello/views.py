from multiprocessing import context
from django.shortcuts import render, HttpResponse

def home(request):
    name = ['soton','turjo','rana']
    context = {
        'name':name
    }
    return render(request, 'home.html', context)
