from django import forms
from .models import Endereco, Cliente


class ClienteForm(forms.Form):

    nome = forms.CharField(max_length=255)
    telefone = forms.CharField(max_length=15)

    cep = forms.IntegerField()
    rua = forms.CharField(max_length=255)
    bairro = forms.CharField(max_length=255)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=255, required=False)
    cidade = forms.CharField(max_length=255)
    estado = forms.ChoiceField(choices=Endereco.estados, widget=forms.Select(attrs={'class': 'form-control'}))
