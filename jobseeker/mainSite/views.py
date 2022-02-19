from django.shortcuts import render
import json,requests
import deso

# Create your views here.
from django.http import HttpResponse

def current_price():
    return deso.Deso().getDeSoPrice()


def home(request):
    return render(request,'home.html',context={"price",current_price()})
