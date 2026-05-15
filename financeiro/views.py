from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Movimentacao
from django.db.models import Sum


def home(request):
    return render(request, 'index.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


def dashboard(request):

    receitas = Movimentacao.objects.filter(
        tipo='RECEITA'
    )

    despesas = Movimentacao.objects.filter(
        tipo='DESPESA'
    )

    total_receitas = receitas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    total_despesas = despesas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    saldo = total_receitas - total_despesas

    movimentacoes = Movimentacao.objects.all().order_by('-data')

    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'movimentacoes': movimentacoes,
    }

    return render(
        request,
        'dashboard.html',
        context
    )