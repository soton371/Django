from multiprocessing import context
from pydoc import render_doc
from unicodedata import name
from django.shortcuts import render, HttpResponse

def home(request):
    name = ['soton','turjo','rana']
    context = {
        'name':name
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name)
        print(phone)
        print(content)
    return render(request,'contact.html')