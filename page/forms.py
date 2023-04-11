from django import forms
class LogIn_Form(forms.Form):
    email = forms.CharField(label="Email",max_length=100)
    password= forms.CharField(label="password",max_length=500)