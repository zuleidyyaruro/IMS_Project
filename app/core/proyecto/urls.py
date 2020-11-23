from django.urls import path

from core.proyecto.views import *

from.import views

urlpatterns = [
    path('lista/', views.Listar_Proyecto.as_view(), name='proyectos_lista'),
    path('crear/', views.Crear_Proyecto.as_view(), name='proyectos_crear'),
    path('actualizar/<pk>', views.Actualizar_Proyecto.as_view(), name='proyectos_actualizar'),
    path('eliminar/<pk>', views.Eliminar_Proyecto.as_view(), name='proyectos_eliminar')
]
