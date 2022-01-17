from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
import random

def  home(request):
    return render(request, 'generator/home.html', )

def  password(request):


    chatacters = list('qwertyuiopsdfghjklzxcvbnm')

    if request.GET.get('uppercase'): # берет из формы
        chatacters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'): # берет из формы
        chatacters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'): # берет из формы
        chatacters.extend(list('1234567890'))

    length = int(request.GET.get('leng' , 12))  # берет из формы <select name="leng"> , 12 по умолчания

    thepass = ''
    for x in range(length):
        thepass += random.choice(chatacters)

    return render(request, 'generator/password.html', {'password': thepass} )

def about(request):
    return  render(request, 'generator/about.html', )