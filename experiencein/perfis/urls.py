from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  # corresponde ao caminho da nossa âncora na página index.html
  path('perfis/<int:perfil_id>', views.exibir)
]
