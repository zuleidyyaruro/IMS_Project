from django.urls import path

from core.integrante.views import *

from.import views

urlpatterns = [
    path('lista/', views.Listar_Integrante.as_view(), name='integrantes_lista'),
    path('crear/', views.Crear_Integrante.as_view(), name='integrantes_crear'),
    path('actualizar/<pk>', views.Actualizar_Integrante.as_view(), name='integrantes_actualizar'),
    path('eliminar/<pk>', views.Eliminar_Integrante.as_view(), name='integrantes_eliminar')
]
