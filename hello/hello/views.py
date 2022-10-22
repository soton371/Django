from multiprocessing import context
from pydoc import render_doc
from unicodedata import name
from django.shortcuts import render, HttpResponse
from tuition.models import Contact

def home(request):
    name = ['soton','turjo','rana']
    context = {
        'name':name
    }
    return render(request, 'home.html', context)

