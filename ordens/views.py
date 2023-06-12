from ordens.models import Peca, Servico, Veiculo, OrdemDeServico

from django.views.generic.list import ListView


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

