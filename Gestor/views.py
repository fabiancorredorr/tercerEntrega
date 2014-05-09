from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def ingresar(request):
    return render_to_response('ingresar.html')


def home(request):
    return render_to_response('home.html')
        
def proyecto1(request):
    return render_to_response('proyecto1.html')
        

def proyectos(request):
    return render_to_response('proyectos.html')
