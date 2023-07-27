from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def display_menu_items(request):
    html = models.menu_items
    return HttpResponse(html)