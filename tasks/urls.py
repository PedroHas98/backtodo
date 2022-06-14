from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('adicionar/addtarefa/', views.addtarefa, name='addtarefa'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('editar/editartarefa/<int:id>', views.editartarefa, name='editartarefa'),
]
