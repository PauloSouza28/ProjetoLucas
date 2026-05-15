from django.db import models
from django.contrib.auth.models import User


class Movimentacao(models.Model):

    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    titulo = models.CharField(
        max_length=100
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    data = models.DateField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo