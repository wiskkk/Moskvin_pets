from django.db import models
from django.db.models import CharField


class Customers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    about = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Pets(models.Model):
    pets = [('c', 'Cat'), ('d', 'Dog'), ('p', 'Pig'), ('r', 'Rabbit'), ('l', 'Lizard')]
    pet_type = models.CharField(max_length=12, choices=pets)
    pet_name = models.CharField(max_length=50)
    pet_img = models.ImageField(upload_to='upload', blank=True)

    customer = models.ForeignKey('Customers', on_delete=models.CASCADE)

    def __str__(self) -> CharField:
        return self.pet_name


class Sitters(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    about = models.TextField(blank=True)
    experience = models.BooleanField(default=False, verbose_name='Have any experience?')

    def __str__(self) -> CharField:
        return self.name
