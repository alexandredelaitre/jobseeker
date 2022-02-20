from telnetlib import Telnet
from django.db import models

class Job (models.Model):
    questBounty=models.TextField(max_length=400)
    questSummary=models.TextField(max_length=400)
    questDesc=models.TextField(max_length=4000)
    questName=models.TextField(max_length=50)


