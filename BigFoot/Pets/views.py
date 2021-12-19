from django.shortcuts import render, redirect

from .forms import AddSitter, AddCustomer, AddPets
from .models import *


def test(request):
    return render(request, 'Pets/test.html', {})


def index(request):
    return render(request, 'Pets/index.html', {})


def about(request):
    return render(request, 'Pets/about.html', {})


def pets(request):
    return render(request, 'Pets/test.html', {})


def pet(request, id):
    return render(request, 'Pets/test.html', {})


# def join(request):
#     return render(request, 'Pets/join.html', {})


def team_reg(request):
    return render(request, 'Pets/team_reg.html', {})


def client_reg(request):
    return render(request, 'Pets/client_reg.html', {})


def choice(request):
    return render(request, 'Pets/choice.html', {})


def sitters(request):
    return render(request, 'Pets/sitters.html', {})


def sitter(request, id):
    return render(request, 'Pets/sitter.html', {})


def add_sitter(request):
    if request.method == "POST":  # the form was submited
        form = AddSitter(request.POST)
        if form.is_valid():
            sitter_entire = Sitters()
            sitter_entire.name = form.cleaned_data['name']
            sitter_entire.surname = form.cleaned_data['surname']
            sitter_entire.email = form.cleaned_data['email']
            sitter_entire.about = form.cleaned_data['about']
            sitter_entire.experience = form.cleaned_data['experience']

            sitter_entire.save()

            return redirect('about')

    else:  # new form should be displayed
        form = AddSitter()

    return render(request, 'Pets/team_reg.html', {'form': form})


def add_customer(request):
    if request.method == "POST":  # the form was submited
        form = AddCustomer(request.POST)
        if form.is_valid():
            customer_entire = Customers()
            customer_entire.name = form.cleaned_data['name']
            customer_entire.surname = form.cleaned_data['surname']
            customer_entire.email = form.cleaned_data['email']
            customer_entire.about = form.cleaned_data['about']

            customer_entire.save()

            return redirect('index')
    else:  # new form should be displayed
        form = AddCustomer()

    return render(request, 'Pets/client_reg.html', {'form': form})
