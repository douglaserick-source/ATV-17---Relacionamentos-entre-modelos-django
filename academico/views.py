from django.shortcuts import render, get_object_or_404
from .models import Projeto, Aluno

# Create your views here.

def lista(request):
    projetos = Projeto.objects.all()
    return render(request, 'academico/lista.html', {'projetos': projetos})


def detalhes_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'academico/detalhe_projeto.html', {'projeto': projeto})


def detalhes_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'academico/detalhe_aluno.html', {'aluno': aluno})