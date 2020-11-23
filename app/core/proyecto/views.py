
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.proyecto.models import Proyecto


class Listar_Proyecto(ListView):
    template_name ='listar_proyecto.html'
    model = Proyecto
    context_object_name = 'lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        return context

class Crear_Proyecto(CreateView):

    template_name="crear_proyecto.html"
    model=Proyecto
    fields=['nombre', 'semillero', 'autores', 'fecha_inicio']
    success_url = reverse_lazy('proyectos_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Proyecto'
        return context


class Actualizar_Proyecto(UpdateView):
    template_name = "actualizar_proyecto.html"
    model = Proyecto
    fields = ['nombre', 'semillero', 'autores', 'fecha_inicio']
    success_url = reverse_lazy('proyectos_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Proyecto'
        return context


class Eliminar_Proyecto(DeleteView):
    template_name = "eliminar_proyecto.html"
    model = Proyecto
    success_url = reverse_lazy('proyectos_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Proyecto'
        return context