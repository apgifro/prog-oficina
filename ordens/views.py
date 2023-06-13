from ordens.models import Peca, Servico, Veiculo, OrdemDeServico

from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import VeiculoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView




class PecasReadView(ListView):

    model = Peca
    ordering = ['-item_id']
    context_object_name = 'pecas'
    template_name = 'pecas/list.html'
    paginate_by = 10


class ServicosReadView(ListView):

    model = Servico
    ordering = ['-item_id']
    context_object_name = 'servicos'
    template_name = 'servicos/list.html'
    paginate_by = 10


class VeiculosReadView(ListView):

    model = Veiculo
    ordering = ['-placa']
    context_object_name = 'veiculos'
    template_name = 'veiculos/list.html'
    paginate_by = 10
    paginate_by = 10


class OrdemReadView(ListView):

    model = OrdemDeServico
    ordering = ['-emitida']
    context_object_name = 'ordens'
    template_name = 'ordem/list.html'
    paginate_by = 10



class VeiculoCreateView(FormView):
    form_class = VeiculoForm
    template_name = 'veiculos/create.html'
    success_url = '/veiculos/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Veículo adicionado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar o veículo.')
        return super().form_invalid(form)

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculos/delete.html'
    success_url = reverse_lazy("veiculos_list")
    slug_field = 'placa'
    slug_url_kwarg = 'placa'

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculos/edit.html'
    success_url = reverse_lazy("veiculos_list")
    slug_field = 'placa'
    slug_url_kwarg = 'placa'