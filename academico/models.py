from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

<<<<<<< HEAD
    def __str__(self):
        return self.nome


=======

    def __str__(self):
        return self.nome
>>>>>>> 81e1e188f90d3f158be305ee4b1d91f9c0c8b7a1
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)

<<<<<<< HEAD
    def __str__(self):
        return self.nome


class PerfilAcademico(models.Model):
    link_lattes = models.URLField()
    biografia = models.TextField()
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return f"Perfil de {self.aluno.nome}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    equipe = models.ManyToManyField(Aluno)

    def __str__(self):
        return self.titulo
=======

    def __str__(self):
        return self.nome
>>>>>>> 81e1e188f90d3f158be305ee4b1d91f9c0c8b7a1
