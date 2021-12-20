from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import AddSitter, AddCustomer, AddPets
from .models import *


def test(request):
    return render(request, 'Pets/test.html', {})


def index(request):
    return render(request, 'Pets/index.html', {})


def about(request):
    return render(request, 'Pets/about.html', {})


def shop(request):
    return render(request, 'Pets/shop.html', {})


def locate(request):
    return render(request, 'Pets/locate.html', {})


def pets(request):
    pets = Pets.objects.all()
    return render(request, 'Pets/pets.html', {'pets': pets})


def pet(request, id):
    try:
        p = Pets.objects.get(id=id)
    except:
        return Http404(request)

    return render(request, 'Pets/pet.html', {"pet": p})


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


def user(request):
    return render(request, 'Pets/user.html', {})


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


# def customer_and_pets(request):
#     if request.method == "POST":  # the form was submited
#         customer_form = AddCustomer(request.POST)
#         pet_form = AddPets(request.POST, request.FILES)
#         if customer_form.is_valid() and pet_form.is_valid():
#             customer_entire = Customers()
#             customer_entire.name = customer_form.cleaned_data['name']
#             customer_entire.surname = customer_form.cleaned_data['surname']
#             customer_entire.email = customer_form.cleaned_data['email']
#             customer_entire.about = customer_form.cleaned_data['about']
#
#             pet_entire = Pets()
#             pet_entire.pet_name = pet_form.cleaned_data['pet_name']
#             pet_entire.pet_type = pet_form.cleaned_data['pet_type']
#             pet_entire.pet_img = pet_form.cleaned_data['pet_img']
#
#             customer_entire.save()
#             pet_entire.save()
#             return redirect('about')
#     else:  # new form should be displayed
#         customer_form = AddCustomer()
#         pet_form = AddPets()
#
#     return render(request, 'Pets/client_reg.html', {
#             'customer_form': customer_form,
#             'pet_form': pet_form,
#         })

def add_customer(request):
    if request.method == "POST":  # the form was submited
        customer_form = AddCustomer(request.POST)
        if customer_form.is_valid():
            customer_entire = Customers()
            customer_entire.name = customer_form.cleaned_data['name']
            customer_entire.surname = customer_form.cleaned_data['surname']
            customer_entire.email = customer_form.cleaned_data['email']
            customer_entire.about = customer_form.cleaned_data['about']

            customer_entire.save()

            return redirect('pet_reg')
    else:  # new form should be displayed
        customer_form = AddCustomer()

    return render(request, 'Pets/client_reg.html', {'customer_form': customer_form})


def add_pets(request):
    if request.method == "POST":  # the form was submited
        pet_form = AddPets(request.POST, request.FILES)
        if pet_form.is_valid():
            pet_entire = Pets()
            pet_entire.pet_name = pet_form.cleaned_data['pet_name']
            pet_entire.pet_type = pet_form.cleaned_data['pet_type']
            pet_entire.pet_img = pet_form.cleaned_data['pet_img']
            # pet_entire.customer = Customers.objects.get(email=request.user.email)
            pet_entire.customer = pet_form.cleaned_data['customer']

            pet_entire.save()

            return redirect('about')
    else:  # new form should be displayed
        pet_form = AddPets()

    return render(request, 'Pets/pet_reg.html', {'pet_form': pet_form})
