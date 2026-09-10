from django.contrib import admin
from .models import Aluno, Projeto, Categoria, PerfilAcademico

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Projeto)
admin.site.register(Categoria)
admin.site.register(PerfilAcademico)