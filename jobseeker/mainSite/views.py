import deso
from django.shortcuts import render
from .forms import JobForm
from .models import Job
import pickle
import json
import uuid

import verification

# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()

def init():
    pickle.dump([], open( "toDoContracts.p", "wb" ))

init()

def home(request):
    mainQuests = pickle.load( open( "toDoContracts.p", "rb" ) )
    postsubmission={}
    quests=[]
    uuidcode=""
    
    if request.method=="POST":
        form=JobForm()
        print(request.POST.keys())
        if form.is_valid():
            form.save()
            context={'form':form}
        try:
            user=request.COOKIES.get('publicKey')
            questName=request.POST['questName']
            summary=request.POST['questSummary']
            questDesc=request.POST['questDesc']
            questBounty=request.POST['questBounty']
            inputs_=eval(request.POST['inputs'])
            outputs_=eval(request.POST['outputs'])
            quests = {
                    'title': questName,
                    'timeAgo': '1m',
                    'description': questDesc,
                    'user': user,
                    'bounty': questBounty,
                    'summary':summary,
                    'uuidcode':uuid.uuid4(),
                    'attempted':False,
                    'complete':False,
                    'attemptedCode':"",
                    'inputs':inputs_,
                    'outputs':outputs_,
                }
            
        except Exception as e:
            print(e)
            uuidcode=request.POST['uuidcode']
            completedCode=request.POST['completedCode']
            postsubmission=completedCode

    if uuidcode!="":
        print(completedCode)
        for i in range(len(mainQuests)):
            if mainQuests[i]['uuidcode']==uuidcode:
                mainQuests[i]['attempted']=True
                mainQuests[i]['attemptedCode']=completedCode
                if verification.parse_and_check_function(completedCode,mainQuests[i]['inputs'],mainQuests[i]['outputs']):
                    mainQuests.remove(mainQuests[i])
                    break
            

    
    if quests!=[]:
        mainQuests.append(quests)

    

    pickle.dump(mainQuests, open( "toDoContracts.p", "wb" ))

    return render(request, 'home.html', context={'quests':mainQuests, 'submission':postsubmission})

# print(current_price()['price_24h'])
