from django.views.generic import FormView

from django.views.generic.list import ListView

from pessoas.forms import ClienteForm
from pessoas.models import Cliente, Mecanico, Equipe, Pessoa, Endereco

from django.contrib import messages


class ClienteListView(ListView):

    model = Cliente
    ordering = ['-pessoa_id']
    context_object_name = 'clientes'
    template_name = 'cliente/list.html'
    paginate_by = 10


class ClienteCreateView(FormView):
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = '/clientes/'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        telefone = form.cleaned_data['telefone']

        cep = form.cleaned_data['cep']
        rua = form.cleaned_data['rua']
        bairro = form.cleaned_data['bairro']
        numero = form.cleaned_data['numero']
        complemento = form.cleaned_data['complemento']
        cidade = form.cleaned_data['cidade']
        estado = form.cleaned_data['estado']

        endereco = Endereco(
            cep=cep, rua=rua, bairro=bairro, numero=numero,
            complemento=complemento, cidade=cidade, estado=estado
        )
        endereco.save()
        pessoa = Pessoa(nome=nome, endereco=endereco)
        pessoa.save()
        cliente = Cliente(pessoa=pessoa, telefone=telefone)
        cliente.save()
        messages.success(self.request, 'Cliente adicionado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar o cliente.')
        print(form.errors)
        return super().form_invalid(form)


# class ClienteUpdateView(FormView):
#     form_class = ClienteForm
#     template_name = 'cliente/create.html'
#     success_url = '/clientes/'
#
#     def form_valid(self, form):
#         nome = form.cleaned_data['nome']
#         telefone = form.cleaned_data['telefone']
#
#         cep = form.cleaned_data['cep']
#         rua = form.cleaned_data['rua']
#         bairro = form.cleaned_data['bairro']
#         numero = form.cleaned_data['numero']
#         complemento = form.cleaned_data['complemento']
#         cidade = form.cleaned_data['cidade']
#         estado = form.cleaned_data['estado']
#
#         endereco = Endereco(
#             cep=cep, rua=rua, bairro=bairro, numero=numero,
#             complemento=complemento, cidade=cidade, estado=estado
#         )
#         endereco.save()
#         pessoa = Pessoa(nome=nome, endereco=endereco)
#         pessoa.save()
#         cliente = Cliente(pessoa=pessoa, telefone=telefone)
#         cliente.save()
#         messages.success(self.request, 'Cliente atualizado.')
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.error(self.request, 'Erro ao atualizar o cliente.')
#         print(form.errors)
#         return super().form_invalid(form)


class MecanicoListView(ListView):

    model = Mecanico
    ordering = ['-pessoa_id']
    context_object_name = 'mecanicos'
    template_name = 'mecanico/list.html'
    paginate_by = 20


class EquipeListView(ListView):

    model = Equipe
    context_object_name = 'equipes'
    ordering = ['-id']
    template_name = 'equipes/list.html'
    paginate_by = 20

