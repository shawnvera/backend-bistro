from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import JsonResponse

# Create your views here.

# response = JsonResponse({"foo:bar"})

def display_menu_item(request):
    html = f'{models.menu_items.title}'
    print(html)
    return JsonResponse(html, safe=False)