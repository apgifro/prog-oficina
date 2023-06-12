from django import forms
from pessoas.models import Endereco, Pessoa, Cliente, Mecanico, Equipe


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ''


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ''


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ''


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ''


class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ''
