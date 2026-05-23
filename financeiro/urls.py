from django.contrib import admin
from django.urls import path
from financeiro.views import (
    home,
    login_view,
    dashboard,
    nova_movimentacao,
    editar_movimentacao,
    excluir_movimentacao,
    logout_view,
    categorias
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('login/', login_view, name='login'),

    path('dashboard/', dashboard, name='dashboard'),

    path(
        'nova-movimentacao/',
        nova_movimentacao,
        name='nova_movimentacao'
    ),

    path(
    'editar-movimentacao/<int:id>/',
    editar_movimentacao,
    name='editar_movimentacao'
    ),

    path(
    'excluir-movimentacao/<int:id>/',
    excluir_movimentacao,
    name='excluir_movimentacao'
    ),

    path(
    'categorias/',
    categorias,
    name='categorias'
),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),
]