from django.urls import path
from . import views  # Importa as views que você vai definir no arquivo views.py

urlpatterns = [
    path('pesquisar/', views.pesquisar_previsao, name='pesquisar_previsao'),
    path('resultado/', views.resultado_previsao, name='resultado_previsao'),
]
