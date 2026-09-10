from django.urls import path
from . import views
app_name = 'academico'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('detalhes_projeto/<int:pk>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('detalhes_aluno/<int:pk>/', views.detalhes_aluno, name='detalhes_aluno'),
]