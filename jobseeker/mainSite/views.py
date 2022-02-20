import deso
from django.shortcuts import render
from .forms import JobForm
from .models import Job

# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()

    

def home(request):
    if request.method=="POST":
        form=JobForm()
        if form.is_valid():
            print("AAAA")
            form.save()
            print("BBBBB")
            context={'form':form}
        
        print(request.POST)
    context={}
    quests = [
        {
            'title': 'Make hello world program',
            'timeAgo': '1m',
            'description': 'I need someone to make a hello world that is really cool',
            'user': 'arara',
            'bounty': str(5)
        }
        
    ]
    
    return render(request, 'home.html', context)

# print(current_price()['price_24h'])
