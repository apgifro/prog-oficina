from django import forms
from pessoas.models import Cliente, Equipe
from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'descricao', 'cliente', 'equipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['equipe'].queryset = Equipe.objects.all()
