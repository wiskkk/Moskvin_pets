from django import forms
from django.core.exceptions import ValidationError

from .models import Pets, Customers, Sitters
from django.forms.fields import Field


class AddPets(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ('pet_type', 'pet_name', 'pet_img', 'customer')


class AddSitter(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    surname = forms.CharField(max_length=50, label='Surname')
    email = forms.EmailField(label='Email')
    image = forms.ImageField(label='Your profile image')
    about = forms.CharField(widget=forms.Textarea, label='About')
    experience = forms.BooleanField(required=False, label='Experience')


setattr(Field, 'is_checkbox', lambda self: isinstance(self.widget, forms.CheckboxInput))


class AddCustomer(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    surname = forms.CharField(max_length=50, label='Surname')
    email = forms.EmailField(label='Email')
    about = forms.CharField(widget=forms.Textarea, label='About')

    # def clean_name(self):
    #     t = self.cleaned_data['name']
    #     self.name = t
    #     if len(t) > 50:
    #         raise ValidationError("The Title is too big")
    #
    #     return t
    #
    # def clean_surname(self):
    #     s = self.cleaned_data['surname']
    #     self.surname = s
    #     if len(s) > 50:
    #         raise ValidationError("The surname is too big")
    #
    #     return s
    #
    # def clean_email(self):
    #     e = self.cleaned_data['email']
    #     self.email = e
    #     for i in e:
    #         if i not in '@.':
    #             raise ValidationError("Incorrect email")
    #
    #     return e
    #
    # def clean_about(self):
    #     a = self.cleaned_data['about']
    #     self.about = a
    #     if len(a) < 5:
    #         raise ValidationError("The about text is too short")
    #
    #     return a


# class AddPets(forms.Form):
#     pets_type = forms.ChoiceField(choices=Pets.pets, label='Pet type')
#     pets_name = forms.CharField(max_length=50, label='Pet name')
#     pets_img = forms.ImageField(label='Pet image')


