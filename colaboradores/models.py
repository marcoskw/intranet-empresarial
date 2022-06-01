from django.db import models
from django.utils import timezone


class Setor(models.Model):
    setor = models.CharField(max_length=255)

    def __str__(self):
        return self.setor


class Cargo(models.Model):
    cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.cargo


class Colaborador(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    setor = models.ForeignKey(Setor, on_delete=models.SET("Vazio"), verbose_name='Setor')
    cargo = models.ForeignKey(Cargo, on_delete=models.SET("Vazio"), verbose_name='Cargo')
    ramal = models.CharField(max_length=255, blank=True, verbose_name='Ramal')
    email = models.CharField(max_length=255, blank=True, verbose_name='Email')
    data_aniversario = models.CharField(max_length=10, blank=True, verbose_name='Aniversário')
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data Criação')
    status = models.BooleanField(default=True, verbose_name='Ativo?')

    def __str__(self):
        return self.nome
