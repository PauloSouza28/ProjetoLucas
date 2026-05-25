from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Movimentacao
from django.db.models import Sum
from .forms import MovimentacaoForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Categoria
from .forms import CategoriaForm
from django.contrib.auth.models import User
from .models import MetaFinanceira
from .forms import MetaFinanceiraForm


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

            return redirect('dashboard')

        else:

            return render(
                request,
                'login.html',
                {
                    'erro': 'Usuário ou senha inválidos'
                }
            )

    return render(request, 'login.html')


@login_required
def dashboard(request):

    movimentacoes = Movimentacao.objects.filter(
        usuario=request.user
    )

    tipo = request.GET.get('tipo')
    categoria = request.GET.get('categoria')
    data = request.GET.get('data')
    busca = request.GET.get('busca')

    if tipo:
        movimentacoes = movimentacoes.filter(
            tipo=tipo
        )

    if categoria:
        movimentacoes = movimentacoes.filter(
            categoria__id=categoria
        )

    if data:
        movimentacoes = movimentacoes.filter(
            data=data
        )

    if busca:
        movimentacoes = movimentacoes.filter(
            titulo__icontains=busca
        )

    receitas = movimentacoes.filter(
        tipo='RECEITA'
    )

    despesas = movimentacoes.filter(
        tipo='DESPESA'
    )

    total_receitas = receitas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    total_despesas = despesas.aggregate(
        Sum('valor')
    )['valor__sum'] or 0

    saldo = total_receitas - total_despesas

    categorias = Categoria.objects.filter(
        usuario=request.user
    )

    context = {
        'movimentacoes': movimentacoes.order_by('-data'),
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'categorias': categorias,
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
def categorias(request):

    form = CategoriaForm()

    if request.method == 'POST':

        form = CategoriaForm(request.POST)

        if form.is_valid():

            categoria = form.save(commit=False)

            categoria.usuario = request.user

            categoria.save()

            return redirect('categorias')

    categorias_receita = Categoria.objects.filter(
        usuario=request.user,
        tipo='RECEITA'
    )

    categorias_despesa = Categoria.objects.filter(
        usuario=request.user,
        tipo='DESPESA'
    )

    context = {
        'form': form,
        'categorias_receita': categorias_receita,
        'categorias_despesa': categorias_despesa,
    }

    return render(
        request,
        'categorias.html',
        context
    )

def cadastro_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        confirmar = request.POST.get('confirmar')

        if password != confirmar:

            return render(
                request,
                'cadastro.html',
                {
                    'erro': 'As senhas não coincidem'
                }
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'cadastro.html',
                {
                    'erro': 'Usuário já existe'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'cadastro.html')

@login_required
def metas(request):

    form = MetaFinanceiraForm()

    if request.method == 'POST':

        form = MetaFinanceiraForm(request.POST)

        if form.is_valid():

            meta = form.save(commit=False)

            meta.usuario = request.user

            meta.save()

            return redirect('metas')

    metas = MetaFinanceira.objects.filter(
        usuario=request.user
    )

    context = {
        'form': form,
        'metas': metas
    }

    return render(
        request,
        'metas.html',
        context
    )

@login_required
def editar_meta(request, id):

    meta = get_object_or_404(
        MetaFinanceira,
        id=id,
        usuario=request.user
    )

    form = MetaFinanceiraForm(
        instance=meta
    )

    if request.method == 'POST':

        form = MetaFinanceiraForm(
            request.POST,
            instance=meta
        )

        if form.is_valid():

            form.save()

            return redirect('metas')

    context = {
        'form': form
    }

    return render(
        request,
        'editar_meta.html',
        context
    )

@login_required
def excluir_meta(request, id):

    meta = get_object_or_404(
        MetaFinanceira,
        id=id,
        usuario=request.user
    )

    meta.delete()

    return redirect('metas')

@login_required
def logout_view(request):

    logout(request)

    return redirect('login')