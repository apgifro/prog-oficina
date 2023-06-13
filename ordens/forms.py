from django import forms
from pessoas.models import Cliente, Equipe
from .models import Veiculo


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
