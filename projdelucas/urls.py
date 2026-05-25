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
    categorias,
    cadastro_view,
    metas,
    editar_meta,
    excluir_meta
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
    'cadastro/',
    cadastro_view,
    name='cadastro'
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

    path(
    'metas/',
    metas,
    name='metas'
),

path(
    'editar-meta/<int:id>/',
    editar_meta,
    name='editar_meta'
),

path(
    'excluir-meta/<int:id>/',
    excluir_meta,
    name='excluir_meta'
),
]