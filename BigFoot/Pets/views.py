from django.shortcuts import render
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


def join(request):
    return render(request, 'Pets/join.html', {})


def sitters(request):
    return render(request, 'Pets/sitters.html', {})


def sitter(request, id):
    return render(request, 'Pets/sitter.html', {})


def login(request):
    return render(request, 'Pets/login.html')
