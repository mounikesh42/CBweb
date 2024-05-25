from django.contrib import admin
from drones.models import Drone

# Register your models here.

@admin.register(Drone)
class JobAdmin(admin.ModelAdmin):
    list_display = ("company_name","drone_description","droneid","expiry")