from django.db import models

# Create your models here.

class Donator(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    slug = models.SlugField(unique=True)
    blood_types_choices = (('A','A+'), ('B','A-'), ('C','B+'),('D', 'B-'), ('E','AB+'),('F','AB-'),('G','O+'),('H','O-'))
    blood_type = models.CharField(max_length=4, choices=blood_types_choices, default='A')
