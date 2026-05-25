from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):

    TIPO_CHOICES = [
        ('RECEITA', 'Receita'),
        ('DESPESA', 'Despesa'),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    nome = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    cor = models.CharField(
        max_length=20,
        default='#38bdf8'
    )

    def __str__(self):
        return self.nome


class MetaFinanceira(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    nome = models.CharField(
        max_length=100
    )

    valor_meta = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    valor_atual = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    prazo = models.DateField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def porcentagem(self):

        if self.valor_meta > 0:

            return int(
                (self.valor_atual / self.valor_meta) * 100
            )

        return 0

    def __str__(self):

        return self.nome


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

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    data = models.DateField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo