from django import forms
from .models import Movimentacao, Categoria
from .models import MetaFinanceira


class MovimentacaoForm(forms.ModelForm):

    class Meta:

        model = Movimentacao

        fields = [
            'tipo',
            'titulo',
            'valor',
            'descricao',
            'categoria',
            'data'
        ]

        widgets = {

            'data': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'tipo': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),

            'categoria': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class CategoriaForm(forms.ModelForm):

    class Meta:

        model = Categoria

        fields = [
            'nome',
            'tipo',
            'cor'
        ]

        widgets = {

            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da categoria'
            }),

            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),

            'cor': forms.TextInput(attrs={
                'type': 'color',
                'class': 'form-control form-control-color'
            }),
        }


class MetaFinanceiraForm(forms.ModelForm):

    class Meta:

        model = MetaFinanceira

        fields = [
            'nome',
            'valor_meta',
            'valor_atual',
            'prazo'
        ]

        widgets = {

            'nome': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'valor_meta': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'valor_atual': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'prazo': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }        