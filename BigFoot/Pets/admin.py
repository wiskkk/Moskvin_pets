from django.contrib import admin
from .models import Customers, Pets, Sitters


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    search_fields = ('name', 'surname')


class SittersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'experience')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname')


class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet_name', 'pet_type', 'pet_img')


admin.site.register(Customers, CustomersAdmin)
admin.site.register(Pets, PetsAdmin)
admin.site.register(Sitters, SittersAdmin)
