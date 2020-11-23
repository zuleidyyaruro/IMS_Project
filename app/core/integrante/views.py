
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.integrante.models import Integrante


class Listar_Integrante(ListView):
    template_name ='listar_integrante.html'
    model = Integrante
    context_object_name = 'lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Integrantes'
        return context

class Crear_Integrante(CreateView):

    template_name="crear_integrante.html"
    model=Integrante
    fields=['nombres', 'correo', 'telefono', 'rol', 'semillero', 'imagen']
    success_url = reverse_lazy('integrantes_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Integrante'
        return context


class Actualizar_Integrante(UpdateView):
    template_name = "actualizar_integrante.html"
    model = Integrante
    fields = ['nombres', 'correo', 'telefono', 'rol', 'semillero', 'imagen']
    success_url = reverse_lazy('integrantes_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Integrante'
        return context


class Eliminar_Integrante(DeleteView):
    template_name = "eliminar_integrante.html"
    model = Integrante
    success_url = reverse_lazy('integrantes_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Integrante'
        return context
