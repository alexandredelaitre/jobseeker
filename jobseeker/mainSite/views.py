import deso
import requests
from django.shortcuts import render

from .forms import JobForm


# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()


def send_message(request):

    publicKey = request.json['publicKey']
    body = request.json['body']

    header = {
        "content-type": "application/json"
    }

    payload = {"UpdaterPublicKeyBase58Check": publicKey,
               "PostHashHexToModify": "",
               "ParentStakeID": "",
               "Title": "",
               "BodyObj": {"Body": body, "ImageURLs": []},
               "RecloutedPostHashHex": "",
               "PostExtraData": {},
               "Sub": "",
               "IsHidden": False,
               "MinFeeRateNanosPerKB": 1000}


    res = requests.post(
        "https://bitclout.com/api/v0/submit-post", json=payload, headers=header)

    resJson = res.json()
    transactionHex = resJson["TransactionHex"]
    print(transactionHex)


def home(request):
    if request.method == "POST":
        form = JobForm()
        print(request.POST.keys())
        if form.is_valid():
            print("AAAA")
            form.save()
            print("BBBBB")
            context = {'form': form}

        print(request.POST['questName'])
        questName = request.POST['questName']
        summary = request.POST['questSummary']
        questDesc = request.POST['questSummary']
        questBounty = request.POST['questSummary']
    context = {}
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
