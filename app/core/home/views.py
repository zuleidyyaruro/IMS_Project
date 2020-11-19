from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Home_View(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Inicio'
        return context

class Información_View(TemplateView):
    template_name = 'informacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Más Información'
        return context

