from django.urls import path
from . import views

items = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

urlpatterns = [
    path('', views.main, name = 'main'),
    path('<str:items>/<int:count>', views.items, name = 'items'),
]
