from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def main(request):
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    contacts = Contact.objects.all()
    teams = Team.objects.all()
    abouts = About.objects.all()

    context = {
        'services':services,
        'portfolios' : portfolios,
        'contacts' : contacts,
        'teams': teams,
        'abouts': abouts,
        'data' : 1
    }
    return render(request, 'index.html', context)