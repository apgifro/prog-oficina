from django import forms
from pessoas.models import Cliente, Equipe
from .models import Veiculo, OrdemDeServico, Item


class PecasForm(forms.Form):

    descricao = forms.CharField(max_length=255)
    preco = forms.FloatField()


class ServicosForm(forms.Form):

    descricao = forms.CharField(max_length=255)
    preco = forms.FloatField()


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'descricao', 'cliente', 'equipe']
        labels = {'placa': 'Placa', 'descricao': 'Descrição'}
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'cliente': forms.Select(attrs={'class': 'form-control mb-4'}),
            'equipe': forms.Select(attrs={'class': 'form-control mb-4'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['equipe'].queryset = Equipe.objects.all()


class OrdemForm(forms.ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = ['entrega', 'veiculo', 'itens', 'total']
        labels = {'veiculo': 'Veículos'}
        widgets = {
            'entrega': forms.SelectDateWidget(attrs={'class': 'form-control mb-4'}),
            'veiculo': forms.Select(attrs={'class': 'form-control mb-4'}),
            'itens': forms.SelectMultiple(attrs={'class': 'form-control mb-4'}),
            'total': forms.TextInput(attrs={'class': 'form-control mb-4'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()
        self.fields['itens'].queryset = Item.objects.all()
