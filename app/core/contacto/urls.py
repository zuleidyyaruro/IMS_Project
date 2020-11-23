from django.urls import path

from core.contacto.views import *

urlpatterns = [
    path('contacto/', contactomail, name='contacto')
]

