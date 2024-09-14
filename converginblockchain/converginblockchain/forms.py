from django import forms
from .models import patientregistrationmodel,docotrtregistrationmodel

class patientregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True,max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    email = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    locality = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}), required=True,max_length=250)
    city = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    state = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting',max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting' ,max_length=100)


    class Meta():
        model = patientregistrationmodel
        fields=['name','loginid','password','mobile','email','locality','address','city','state','authkey','status']


class doctorregistrationform(forms.ModelForm):
    doctorname = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True,max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    emailid = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    locality = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 30}), required=True,max_length=250)
    city = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    state = forms.CharField(widget=forms.TextInput(), required=True,max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting',max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting' ,max_length=100)


    class Meta():
        model = docotrtregistrationmodel
        fields=['doctorname','loginid','password','mobile','emailid','locality','address','city','state','authkey','status']

        
    

