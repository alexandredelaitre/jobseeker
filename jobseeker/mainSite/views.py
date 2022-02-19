from django.shortcuts import render
import json,requests
import deso

# Create your views here.
from django.http import HttpResponse

def current_price():
    return deso.Deso().getDeSoPrice()




def home(request):
    quests=[{'title':'Make hello world program','timeAgo':'1m','description':'I need someone to make a hello world that is really cool','bounty':str(5)}]
    return render(request,'home.html',context={'quests':quests})

#print(current_price()['price_24h'])