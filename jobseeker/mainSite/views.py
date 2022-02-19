import deso
from django.shortcuts import render


# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()


def home(request):
    quests = [
        {
            'title': 'Make hello world program',
            'timeAgo': '1m',
            'description': 'I need someone to make a hello world that is really cool',
            'user': 'arara',
            'bounty': str(5)
        }
    ]
    return render(request, 'home.html', context={'quests': quests})

# print(current_price()['price_24h'])
