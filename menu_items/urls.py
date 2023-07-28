from django.urls import path, include
from . import views

urlpatterns = [
    path('display_menu_item/', views.display_menu_item, name='display_menu_item'),
]
