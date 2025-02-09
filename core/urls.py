from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]
