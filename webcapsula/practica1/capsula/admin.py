from django.contrib import admin
from .models import Service, About, Client, Team, Portfolio

# Register your models here.
admin.site.register([Service, About, Client, Team, Portfolio])