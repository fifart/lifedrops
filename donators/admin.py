from django.contrib import admin
from random import randint

# Register your models here.
from donators.models import Donator

class DonatorAdmin(admin.ModelAdmin):
    model = Donator
    und = range(1000,9999)	
    list_display = ('name', 'phone', 'address', 'blood_type',)
    prepopulated_fields = {'slug':('name','blood_type',)}

admin.site.register(Donator, DonatorAdmin)
