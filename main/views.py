from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

# for model called PORTFOLIO #############################################################
def get_portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios':portfolios}
    return HttpResponse('data was returned in portfolios')

def create_portfolio(request):
    portfolios = Portfolio.objects.create(...) # ushbu qism hali o'tilmagan
    return HttpResponse('data was created in portfolios')

def update_portfolio(request):
    portf = Portfolio.objects.get(id = 1)
    portf.title = 'Banner design'
    return HttpResponse('data was updated in portfolios')

def del_portfolio(request):
    portf = Portfolio.objects.get(id = 4)
    portf.delete()
    return HttpResponse('data was removed in portfolios')



# for model called CONTACT #############################################################
def get_contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return HttpResponse('data was returned in contact')

def create_contact(request):
    contacts = Contact.objects.create(...) # ushbu qism hali o'tilmagan
    return HttpResponse('data was created in contact')

def update_contact(request):
    contact = Contact.objects.get(id = 2)
    contact.phone = '+998905819435'
    return HttpResponse('data was updated in contact')

def del_contact(request):
    contact = Contact.objects.get(id = 1)
    contact.delete()
    return HttpResponse('data was deleted in contact')


# for model called SERVICE #############################################################
def get_service(request):
    service = Service.objects.all()
    context = {'service':service}
    return HttpResponse('data was returned in service')

def create_service(request):
    service = Service.objects.create(...) # ushbu qism hali o'tilmagan
    return HttpResponse('data was created in service')

def update_service(request):
    service = Service.objects.get(id = 2)
    service.title = 'Designing'
    return HttpResponse('data was updated in service')

def del_service(request):
    service = Service.objects.get(id = 1)
    service.delete()
    return HttpResponse('data was deleted in service')



# for model called ABOUT #############################################################
def get_about(request):
    all_about = About.objects.all()
    context = {'about':all_about}
    return HttpResponse('data was returned in about')

def create_about(request):
    one_about = About.objects.create(...) # ushbu qism hali o'tilmagan
    return HttpResponse('data was created in about')

def update_about(request):
    about = About.objects.get(id = 2)
    about.title = 'Fast'
    return HttpResponse('data was updated in about')

def del_about(request):
    about = About.objects.get(id = 1)
    about.delete()
    return HttpResponse('data was deleted in about')



# for model called TEAM #############################################################
def get_team(request):
    teams = Team.objects.all()
    context = {'teams':teams}
    return HttpResponse('data was returned in team')

def create_team(request):
    team = Team.objects.create(...) # ushbu qism hali o'tilmagan
    return HttpResponse('data was created in team')

def update_team(request):
    team = Team.objects.get(id = 2)
    team.role = 'Manager'
    return HttpResponse('data was updated in team')

def del_team(request):
    team = Team.objects.get(id = 1)
    team.delete()
    return HttpResponse('data was deleted in team')

