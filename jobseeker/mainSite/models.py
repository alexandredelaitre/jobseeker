from telnetlib import Telnet
from django.db import models

class Job (models.Model):
    questBounty=models.TextField(max_length=400)
    questSummary=models.TextField(max_length=400)
    questDesc=models.TextField(max_length=4000)
    questName=models.TextField(max_length=50)

class Code (models.Model):
    uuidcode=models.TextField(max_length=400)
    completedCode=models.TextField(max_length=25000)
    file = forms.FileField()

