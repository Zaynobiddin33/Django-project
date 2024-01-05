from django.urls import path
from .views import *
urlpatterns =[
    path('get/portfolio', get_portfolio),
    path('updt/portfolio', update_portfolio),
    path('create/portfolio', create_portfolio),
    path('del/portfolio', del_portfolio),

    path('get/contact', get_contacts),
    path('updt/contact', update_contact),
    path('create/contact', create_contact),
    path('del/contact', del_contact),

    path('get/service', get_service),
    path('updt/service', update_service),
    path('create/service', create_service),
    path('del/service', del_service),

    path('get/about', get_about),
    path('updt/about', update_about),
    path('create/about', create_about),
    path('del/about', del_about),

    path('get/team', get_team),
    path('updt/team', update_team),
    path('create/team', create_team),
    path('del/team', del_team),
]