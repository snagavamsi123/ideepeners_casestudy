from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django.forms.fields import Field
from .models import signup,DailyUpdate,ClientDetails

class signupform(ModelForm):
    class Meta:
        model = signup
        fields = '__all__'
        widgets={
            'Password':forms.PasswordInput(render_value=True),
        }


class loginform(ModelForm):
    class Meta:
        model = signup
        fields = ('Mobile' or 'Email','Password')
        widgets={
            'Password':forms.PasswordInput(render_value=True),
        }

class DailyUpdateForm(ModelForm):
    class Meta:
        model = DailyUpdate
        fields = ('Area','AppointedPersons','NoOfClients')
class ClientDetailsField(ModelForm):
    class Meta:
        model = ClientDetails
        fields = '__all__'
        widgets={
            'DateOfBirth':widgets.SelectDateWidget(years=range(1900,2021)),
        }