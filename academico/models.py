from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)


    def __str__(self):
        return self.nome
