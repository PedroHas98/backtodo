from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/', views.logar_usuario, name="logar_usuario"),
    path('principal/', views.logar_usuario, name="principal"),
]

