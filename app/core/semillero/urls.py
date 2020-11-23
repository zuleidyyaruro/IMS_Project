from django.urls import path

from core.semillero.views import *

from.import views

urlpatterns = [
    path('lista/', views.Listar_Semillero.as_view(), name='semilleros_lista'),
    path('crear/', views.Crear_Semillero.as_view(), name='semilleros_crear'),
    path('actualizar/<pk>', views.Actualizar_Semillero.as_view(), name='semilleros_actualizar'),
    path('eliminar/<pk>', views.Eliminar_Semillero.as_view(), name='semilleros_eliminar')
]
