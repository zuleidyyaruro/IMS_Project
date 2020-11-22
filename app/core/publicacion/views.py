

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.publicacion.models import Publicacion


class Listar_Publicaciones(ListView):
    template_name ='listar.html'
    model = Publicacion
    context_object_name = 'lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Publicaciones'
        return context

class Crear_publicacion(CreateView):

    template_name="crear.html"
    model=Publicacion
    fields=['nombre', 'tipo_publicacion', 'autores', 'anio_publicacion']
    success_url = reverse_lazy('publicaciones_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Publicación'
        return context


class Actualizar_publicacion(UpdateView):
    template_name = "actualizar.html"
    model = Publicacion
    fields = ['nombre', 'tipo_publicacion', 'autores', 'anio_publicacion']
    success_url = reverse_lazy('publicaciones_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Publicación'
        return context


class Eliminar_Publicación(DeleteView):
    template_name = "eliminar.html"
    model = Publicacion
    success_url = reverse_lazy('publicaciones_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Publicación'
        return context