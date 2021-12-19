from django import forms
from django.forms import inlineformset_factory

from .models import Pets, Customers
from django.forms.fields import Field


class AddSitter(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    surname = forms.CharField(max_length=50, label='Surname')
    email = forms.EmailField(label='Email')
    about = forms.CharField(widget=forms.Textarea, label='About')
    experience = forms.BooleanField(required=False, label='Experience')


setattr(Field, 'is_checkbox', lambda self: isinstance(self.widget, forms.CheckboxInput))


class AddCustomer(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    surname = forms.CharField(max_length=50, label='Surname')
    email = forms.EmailField(label='Email')
    about = forms.CharField(widget=forms.Textarea, label='About')


class AddPets(forms.Form):
    pets_type = forms.ChoiceField(choices=Pets.pets, label='Pet type')
    pets_name = forms.CharField(max_length=50, label='Pet name')
    pets_img = forms.ImageField(label='Pet image')
    about = forms.CharField(widget=forms.Textarea, label='About')



