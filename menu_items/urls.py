from django.urls import path, include
from . import views

urlpatterns = [
    path('menu_items/', views.display_menu_item),
]
