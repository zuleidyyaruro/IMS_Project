from django.urls import path

from core.publicacion.views import *
from.import views

urlpatterns = [
    path('lista/', views.Listar_Publicaciones.as_view(), name='publicaciones_lista'),
    path('crear/', views.Crear_publicacion.as_view(), name='publicaciones_crear'),
    path('actualizar/<pk>', views.Actualizar_publicacion.as_view(), name='publicaciones_actualizar'),
    path('eliminar/<pk>', views.Eliminar_Publicación.as_view(), name='publicaciones_eliminar')
]
