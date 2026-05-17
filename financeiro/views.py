from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Movimentacao
from django.db.models import Sum
from .forms import MovimentacaoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


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


@login_required
def dashboard(request):

    receitas = Movimentacao.objects.filter(
    usuario=request.user,
    tipo='RECEITA'
    )

    despesas = Movimentacao.objects.filter(
    usuario=request.user,
    tipo='DESPESA'
    )

    total_receitas = receitas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    total_despesas = despesas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    saldo = total_receitas - total_despesas

    movimentacoes = Movimentacao.objects.filter(
    usuario=request.user
    ).order_by('-data')

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

@login_required
def nova_movimentacao(request):

    form = MovimentacaoForm()

    if request.method == 'POST':

        form = MovimentacaoForm(request.POST)

        if form.is_valid():

            movimentacao = form.save(commit=False)

            movimentacao.usuario = request.user

            movimentacao.save()

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'nova_movimentacao.html',
        context
    )

@login_required
def editar_movimentacao(request, id):

    movimentacao = get_object_or_404(
        Movimentacao,
        id=id,
        usuario=request.user
    )

    form = MovimentacaoForm(
        instance=movimentacao
    )

    if request.method == 'POST':

        form = MovimentacaoForm(
            request.POST,
            instance=movimentacao
        )

        if form.is_valid():

            form.save()

            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(
        request,
        'editar_movimentacao.html',
        context
    )

@login_required
def excluir_movimentacao(request, id):

    movimentacao = get_object_or_404(
        Movimentacao,
        id=id,
        usuario=request.user
    )

    movimentacao.delete()

    return redirect('dashboard')

@login_required
def logout_view(request):

    logout(request)

    return redirect('login')