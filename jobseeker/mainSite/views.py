import deso
from django.shortcuts import render
from .forms import JobForm
from .models import Job
import pickle
import json
import uuid



# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()

def init():
    pickle.dump([], open( "toDoContracts.p", "wb" ))

#init()

def home(request):
    mainQuests = pickle.load( open( "toDoContracts.p", "rb" ) )
    postsubmission={}
    quests=[]
    uuidcode=""
    
    if request.method=="POST":
        form=JobForm()
        print(request.POST.keys())
        if form.is_valid():
            print("AAAA")
            form.save()
            print("BBBBB")
            context={'form':form}
        try:
            user=request.COOKIES.get('publicKey')
            questName=request.POST['questName']
            summary=request.POST['questSummary']
            questDesc=request.POST['questDesc']
            questBounty=request.POST['questBounty']
            quests = {
                    'title': questName,
                    'timeAgo': '1m',
                    'description': questDesc,
                    'user': user,
                    'bounty': questBounty,
                    'summary':summary,
                    'uuid':uuid.uuid4(),
                    'attempted':False,
                    'complete':False,
                    'attemptedCode':""
                }
            
        except:
            uuidcode=request.POST['uuidcode']
            completedCode=request.POST['completedCode']
            postsubmission=completedCode

    if uuidcode!="":   
        for i in range(len(mainQuests)):
            if mainQuests[i]['uuid']==uuidcode:
                mainQuests[i]['attempted']=True
                mainQuests[i]['attemptedCode']=completedCode

    
    if quests!=[]:
        mainQuests.append(quests)



    pickle.dump(mainQuests, open( "toDoContracts.p", "wb" ))

    return render(request, 'home.html', context={'quests':mainQuests, 'submission':postsubmission})

# print(current_price()['price_24h'])
