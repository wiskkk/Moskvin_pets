from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test/', test),
    path('about/', about, name='about'),
    path('pets/', pets, name='pets'),
    path('pets/<int:id>/', pet, name='pet'),
    path('sitters/', sitters, name='sitters'),
    path('sitters/<int:id>/', sitter, name='sitter'),
    path('join/', add_sitter, name='add_sit'),
    # path('join/', join, name='join'),
    path('choice/', choice, name='choice'),
    path('team_reg/', team_reg, name='team_reg'),
    path('client_reg/', client_reg, name='client_reg'),
    # path('add_sit/', add_sitter, name='add_sit'),

]
