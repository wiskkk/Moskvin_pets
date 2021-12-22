from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test/', test),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('pets/', pets, name='pets'),
    path('pets/<int:id>/', pet, name='pets'),
    path('sitters/', sitters, name='sitters'),
    path('sitters/<int:id>/', sitter, name='sitter'),
    path('choice/', choice, name='choice'),
    path('team_reg/', add_sitter, name='team_reg'),
    path('client_reg/', add_customer, name='client_reg'),
    path('pet_reg/', add_pets, name='pet_reg'),
    path('locate/', locate, name='locate'),

]
