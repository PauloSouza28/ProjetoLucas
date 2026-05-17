from django import forms
from .models import Movimentacao


class MovimentacaoForm(forms.ModelForm):

    class Meta:
        model = Movimentacao

        fields = [
            'tipo',
            'titulo',
            'valor',
            'descricao',
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
        }