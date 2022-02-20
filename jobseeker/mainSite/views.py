import deso
from django.shortcuts import render
from .forms import JobForm, CodeUpload
import pickle
import uuid
import verification
from django.http import HttpResponseRedirect


# Create your views here.

def current_price():
    return deso.Deso().getDeSoPrice()


def init():
    pickle.dump([], open("toDoContracts.p", "wb"))


# init()


def upload_file(request):
    if request.method == 'POST':
        form = CodeUpload(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            inputs = [[1, 1], [1, 0], [1, -1], [10, 11]]
            outputs = [2, 1, 0, 21]
            try:
                res = verification.parse_and_check_function(''.join(request.FILES['file'].readlines()), inputs, outputs)
            except BaseException:
                res = False
            if res:
                return HttpResponseRedirect('/success/url/')
            else:
                return HttpResponseRedirect('/fail/url/')
    else:
        form = CodeUpload()
    return render(request, 'home.html', {'form': form})


def home(request):
    mainQuests = pickle.load(open("toDoContracts.p", "rb"))
    postsubmission = {}
    quests = []
    uuidcode = ""

    if request.method == 'POST':
        form2 = CodeUpload(request.POST, request.FILES)
        if form2.is_valid():
            handle_uploaded_file(request.FILES['file'])

            return HttpResponseRedirect('/success/url/')
    else:
        form = CodeUpload()

    if request.method == "POST":
        form = JobForm()
        print(request.POST.keys())
        if form.is_valid():
            print("AAAA")
            form.save()
            print("BBBBB")
            context = {'form': form}
        try:
            user = request.COOKIES.get('publicKey')
            questName = request.POST['questName']
            summary = request.POST['questSummary']
            questDesc = request.POST['questDesc']
            questBounty = request.POST['questBounty']
            quests = {
                'title': questName,
                'timeAgo': '1m',
                'description': questDesc,
                'user': user,
                'bounty': questBounty,
                'summary': summary,
                'uuid': uuid.uuid4(),
                'attempted': False,
                'complete': False,
                'attemptedCode': ""
            }

        except:
            uuidcode = request.POST['uuidcode']
            completedCode = request.POST['completedCode']
            postsubmission = completedCode

    if uuidcode != "":
        for i in range(len(mainQuests)):
            if mainQuests[i]['uuid'] == uuidcode:
                mainQuests[i]['attempted'] = True
                mainQuests[i]['attemptedCode'] = completedCode

    if quests != []:
        mainQuests.append(quests)

    pickle.dump(mainQuests, open("toDoContracts.p", "wb"))

    return render(request, 'home.html', context={'quests': mainQuests, 'submission': postsubmission})

# print(current_price()['price_24h'])
