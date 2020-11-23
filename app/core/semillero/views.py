
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.semillero.models import Semillero


class Listar_Semillero(ListView):
    template_name ='listar_semillero.html'
    model = Semillero
    context_object_name = 'lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Semilleros'
        return context

class Crear_Semillero(CreateView):

    template_name="crear_semillero.html"
    model=Semillero
    fields=['nombre', 'linea_investigacion', 'anio_constitucion', 'director', 'correo', 'telefono']
    success_url = reverse_lazy('semilleros_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Semillero'
        return context


class Actualizar_Semillero(UpdateView):
    template_name = "actualizar_semillero.html"
    model = Semillero
    fields = ['nombre', 'linea_investigacion', 'anio_constitucion', 'director', 'correo', 'telefono']
    success_url = reverse_lazy('semilleros_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Semillero'
        return context


class Eliminar_Semillero(DeleteView):
    template_name = "eliminar_semillero.html"
    model = Semillero
    success_url = reverse_lazy('semilleros_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Semillero'
        return context