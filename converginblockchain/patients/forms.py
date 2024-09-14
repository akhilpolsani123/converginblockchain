from django import forms
from .models import patientsymptomsanalysis

class patientsymptomsanalysisform(forms.ModelForm):

    class Meta:
        model = patientsymptomsanalysis
        fields = ['patintid','patinetname','email','patinetallsymptoms','diseasname','descriptions','createdon']

