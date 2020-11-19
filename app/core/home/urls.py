from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.Home_View.as_view(), name='index'),  # clase PruebaView del archivo views.py
    path('mas_informacion/', views.Información_View.as_view(), name='informacion')
]
