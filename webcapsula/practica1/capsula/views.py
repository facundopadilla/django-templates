from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    print(range(len(About.objects.all())))
    return render(request, 'capsula/index.html', {
        'services':Service.objects.all(),
        'portfolios':[i for i in Portfolio.objects.all()],
        'abouts':[i for i in About.objects.all()],
        'teams':Team.objects.all(),
        'clients':Client.objects.all(),
        'range_about':range(len(About.objects.all())),
        'range_team':range(len(Team.objects.all())),
        'range_portfolio':range(len(Portfolio.objects.all())),
        'range_client':range(len(Client.objects.all()))
    })
    