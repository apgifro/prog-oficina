from ordens.models import Peca, Servico, Veiculo, OrdemDeServico, Item

from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import VeiculoForm, PecasForm, ServicosForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView


class PecasReadView(ListView):

    model = Peca
    ordering = ['-item_id']
    context_object_name = 'pecas'
    template_name = 'pecas/list.html'
    paginate_by = 10


class PecasCreateView(FormView):
    form_class = PecasForm
    template_name = 'pecas/create.html'
    success_url = '/pecas/'

    def form_valid(self, form):
        descricao = form.cleaned_data['descricao']
        preco = form.cleaned_data['preco']

        item = Item(descricao=descricao, preco=preco)
        item.save()

        peca = Peca(item=item)
        peca.save()

        messages.success(self.request, 'Peça adicionada.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar a peça.')
        print(form.errors)
        return super().form_invalid(form)


class PecasUpdateView(FormView):
    form_class = PecasForm
    template_name = 'pecas/edit.html'
    success_url = '/pecas/'

    def get_peca(self, id_post):
        try:
            return Peca.objects.get(pk=id_post)
        except Peca.DoesNotExist:
            messages.error(self.request, 'A peça não existe!')
            reverse_lazy('pecas_list')

    def get_context_data(self, **kwargs):
        context = super(PecasUpdateView, self).get_context_data(**kwargs)
        context['peca'] = self.get_peca(self.kwargs['pk'])
        return context

    def form_valid(self, form):

        descricao = form.cleaned_data['descricao']
        preco = form.cleaned_data['preco']

        peca = self.get_context_data()['peca']
        item = peca.item
        item.descricao = descricao
        item.preco = preco

        item.save()
        peca.save()

        messages.success(self.request, 'Peça atualizada.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar a peça.')
        print(form.errors)
        return super().form_invalid(form)


class PecasDeleteView(DeleteView):
    model = Peca
    template_name = 'pecas/delete.html'
    success_url = reverse_lazy("pecas_list")


class ServicosReadView(ListView):

    model = Servico
    ordering = ['-item_id']
    context_object_name = 'servicos'
    template_name = 'servicos/list.html'
    paginate_by = 10


class ServicosCreateView(FormView):
    form_class = ServicosForm
    template_name = 'servicos/create.html'
    success_url = '/servicos/'

    def form_valid(self, form):
        descricao = form.cleaned_data['descricao']
        preco = form.cleaned_data['preco']

        item = Item(descricao=descricao, preco=preco)
        item.save()

        servico = Servico(item=item)
        servico.save()

        messages.success(self.request, 'Serviço adicionada.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar o serviço.')
        print(form.errors)
        return super().form_invalid(form)


class ServicosUpdateView(FormView):
    form_class = ServicosForm
    template_name = 'servicos/edit.html'
    success_url = '/servicos/'

    def get_servico(self, id_post):
        try:
            return Servico.objects.get(pk=id_post)
        except Peca.DoesNotExist:
            messages.error(self.request, 'O serviço não existe!')
            reverse_lazy('pecas_list')

    def get_context_data(self, **kwargs):
        context = super(ServicosUpdateView, self).get_context_data(**kwargs)
        context['servico'] = self.get_servico(self.kwargs['pk'])
        return context

    def form_valid(self, form):

        descricao = form.cleaned_data['descricao']
        preco = form.cleaned_data['preco']

        servico = self.get_context_data()['servico']
        item = servico.item
        item.descricao = descricao
        item.preco = preco

        item.save()
        servico.save()

        messages.success(self.request, 'Serviço atualizado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar o serviço.')
        print(form.errors)
        return super().form_invalid(form)


class ServicosDeleteView(DeleteView):
    model = Servico
    template_name = 'servicos/delete.html'
    success_url = reverse_lazy("servicos_list")


class VeiculosReadView(ListView):

    model = Veiculo
    ordering = ['-placa']
    context_object_name = 'veiculos'
    template_name = 'veiculos/list.html'
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
