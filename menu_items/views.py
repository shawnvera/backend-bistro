from django.shortcuts import render
from django.http import HttpResponse
from .models import menu_items
from django.http import JsonResponse


# Create your views here.

def display_menu_item(request):
    data = []
    Menu_items = menu_items.objects.all()
    for item in Menu_items:
        data.append({'id':item.id,
                     'title': item.title,
                     'description': item.description,
                     'price': item.price,
                     'spicy level': item.spicy_level,
                     'category': item.category_id,
                     'cuisine': item.cuisine_id,

                     })
    # html = f'{menu_items.title}' + f'{menu_items.spicy_level}'
    print(Menu_items)
    return JsonResponse(data, safe=False)
    # print(JsonResponse(data, safe=False))

    