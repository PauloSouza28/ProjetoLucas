from django import forms
from .models import Movimentacao, Categoria


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