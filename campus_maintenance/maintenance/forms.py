from django import forms
from .models import MaintenanceRequest
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    password=forms.CharField(
        widget=forms.PasswordInput
    )


    class Meta:
        model=User

        fields=[
            'username',
            'email',
            'password'
        ]



class MaintenanceForm(forms.ModelForm):

    class Meta:

        model=MaintenanceRequest

        fields=[
            'title',
            'description',
            'category',
            'location',
            'priority'
        ]