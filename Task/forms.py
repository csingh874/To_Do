from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = user_Task
        fields = "__all__"
        widgets = {
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "descreption":forms.TextInput(attrs={"class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class UserFormCreation(UserCreationForm):

    password1 = forms.CharField(widget =forms.PasswordInput( attrs={"class":"form-control","type":"password"}))
    password2 = forms.CharField(widget =forms.PasswordInput( attrs={"class":"form-control","type":"password"}))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),


        }

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("old_password","new_password1","new_password2")

