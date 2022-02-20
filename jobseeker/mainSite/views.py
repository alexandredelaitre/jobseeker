import pickle
import uuid

import deso
from django.shortcuts import render

from .forms import JobForm

from twilio.rest import Client
import dotenv
import os

dotenv.load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_SID']

# Your Auth Token from twilio.com/console
auth_token = os.environ['TWILIO_SECRET']

client = Client(account_sid, auth_token)

def send_message(msg):
    client.messages.create(
        to="+447579065474",
        from_="+447700158128",
        body=msg)



inputs = [[1, 1], [1, 0], [1, -1], [10, 11]]
outputs = [2, 1, 0, 21]


def check_function(func, inputs, outputs):
    for n in range(len(inputs)):
        i = inputs[n]
        out = func(*i)
        if outputs[n] != out:
            return False
    return True


def parse_and_check_function(func_str, inputs, outputs):
    for n in range(len(inputs)):

        i = inputs[n]
        args = ""
        if isinstance(i, list):
            args = ",".join(str(a) for a in i)
        else:
            args = str(i)
        ex_locals = {}
        exec(func_str + '\n' +
             'zzzzzzzzzzzzzzzzzzzzzzz = ((main(' + args + ')) ==' + str(outputs[n]) + ')', {"built": __builtins__},
             ex_locals
             )

        if not bool(ex_locals['zzzzzzzzzzzzzzzzzzzzzzz']):
            return False
    return True


def parse_and_check_filename(filename, inputs, outputs):
    file = open(filename, 'r').readlines()
    return parse_and_check_function(''.join(file), inputs, outputs)


# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()


def init():
    pickle.dump([], open("toDoContracts.p", "wb"))


def home(request):
    mainQuests = pickle.load(open("toDoContracts.p", "rb"))
    postsubmission = {}
    quests = []
    uuidcode = ""

    if request.method == "POST":
        form = JobForm()


def home(request):
    mainQuests = pickle.load(open("toDoContracts.p", "rb"))
    postsubmission = {}
    quests = []
    uuidcode = ""

    if request.method == "POST":
        form = JobForm()
        print(request.POST.keys())
        if form.is_valid():
            form.save()
            context = {'form': form}
        try:
            user = request.COOKIES.get('publicKey')
            questName = request.POST['questName']
            summary = request.POST['questSummary']
            questDesc = request.POST['questDesc']
            questBounty = request.POST['questBounty']
            inputs_ = eval(request.POST['inputs'])
            outputs_ = eval(request.POST['outputs'])
            quests = {
                'title': questName,
                'timeAgo': '1m',
                'description': questDesc,
                'user': user,
                'bounty': questBounty,
                'summary': summary,
                'uuidcode': uuid.uuid4(),
                'attempted': False,
                'complete': False,
                'attemptedCode': "",
                'inputs': inputs_,
                'outputs': outputs_,
            }

        except Exception as e:
            print(e)
            uuidcode = request.POST['uuidcode']
            completedCode = request.POST['completedCode']
            postsubmission = completedCode

    if uuidcode != "":
        print(uuidcode)
        print(completedCode)
        print(mainQuests)
        print(type(mainQuests[0]['inputs']))
        for i in range(len(mainQuests)):
            if str(mainQuests[i]['uuidcode']) == uuidcode:
                print("found")

                mainQuests[i]['attempted'] = True
                mainQuests[i]['attemptedCode'] = completedCode
                if parse_and_check_function(completedCode, mainQuests[i]['inputs'], mainQuests[i]['outputs']):
                    send_message("Your task has been completed!")
                    mainQuests.remove(mainQuests[i])
                    break

    if quests != []:
        mainQuests.append(quests)

    pickle.dump(mainQuests, open("toDoContracts.p", "wb"))

    return render(request, 'home.html', context={'quests': mainQuests, 'submission': postsubmission, 'completed': True})

# print(current_price()['price_24h'])
