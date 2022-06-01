from django.shortcuts import render
from .models import Colaborador


def index(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores/index.html', {
        'colaboradores': colaboradores
    })


def ver_colaborador(request, colaborador_id):
    colaborador = Colaborador.objects.get(id=colaborador_id)
    return render(request, 'colaboradores/ver_colaborador.html', {
        'colaborador': colaborador
    })
