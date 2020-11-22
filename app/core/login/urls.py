from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [


    path('', TemplateView.as_view(template_name="login.html")),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
