from django import forms
from .models import signup

class Abdi(forms.Form):
    Full_Name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Full Name'
    }))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your E-Mail'
    }))
    User_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your UserName'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Password'
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Phone'
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Address'
    }))
