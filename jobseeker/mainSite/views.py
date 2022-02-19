from django.shortcuts import render
import json,requests


# Create your views here.
from django.http import HttpResponse

contractDecimals=18

def home(request):
    return render(request,'home.html')
