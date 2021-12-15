from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('pets/', pets, name='pets'),
    path('pets/<int:id>/', pet, name='pet'),
    path('sitters/', sitters, name='sitters'),
    path('sitters/<int:id>/', sitter, name='sitter'),
]

