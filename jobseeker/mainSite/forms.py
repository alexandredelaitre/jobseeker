
from django import forms
from .models import Job,Code

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        
class CodeForm(forms.ModelForm):
    class Meta:
        model=Code
        fields='__all__'
        
class CodeUpload(forms.Form):
    file = forms.FileField()