from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView, UpdateView

from django.views.generic.list import ListView

from pessoas.forms import ClienteForm, MecanicoForm, EquipeForm
from pessoas.models import Cliente, Mecanico, Equipe, Pessoa, Endereco

from django.contrib import messages


class ClienteReadView(ListView):

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


class ClienteUpdateView(FormView):
    form_class = ClienteForm
    template_name = 'cliente/edit.html'
    success_url = '/clientes/'

    def get_cliente(self, id_post):
        try:
            return Cliente.objects.get(pk=id_post)
        except Cliente.DoesNotExist:
            messages.error(self.request, 'O cliente não existe!')
            reverse_lazy('clientes_list')

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context['cliente'] = self.get_cliente(self.kwargs['pk'])
        self.initial['estado'] = context['cliente'].pessoa.endereco.estado # BUG
        return context

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

        cliente = self.get_context_data()['cliente']
        endereco = cliente.pessoa.endereco

        endereco.cep = cep
        endereco.rua = rua
        endereco.bairro = bairro
        endereco.numero = numero
        endereco.complemento = complemento
        endereco.cidade = cidade
        endereco.estado = estado
        endereco.save()

        pessoa = cliente.pessoa
        pessoa.nome = nome
        pessoa.save()

        cliente.telefone = telefone
        cliente.pessoa = pessoa
        cliente.save()

        messages.success(self.request, 'Cliente atualizado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar o cliente.')
        print(form.errors)
        return super().form_invalid(form)


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/delete.html'
    success_url = reverse_lazy("clientes_list")


class MecanicoListView(ListView):

    model = Mecanico
    ordering = ['-pessoa_id']
    context_object_name = 'mecanicos'
    template_name = 'mecanico/list.html'
    paginate_by = 20


class MecanicoCreateView(FormView):
    form_class = MecanicoForm
    template_name = 'mecanico/create.html'
    success_url = '/mecanicos/'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        especialidade = form.cleaned_data['especialidade']

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
        mecanico = Cliente(pessoa=pessoa, especialidade=especialidade)
        mecanico.save()
        messages.success(self.request, 'Mecânico adicionado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar o mecânico.')
        print(form.errors)
        return super().form_invalid(form)


class MecanicoUpdateView(FormView):
    form_class = MecanicoForm
    template_name = 'mecanico/edit.html'
    success_url = '/mecanicos/'

    def get_mecanico(self, id_post):
        try:
            return Mecanico.objects.get(pk=id_post)
        except Mecanico.DoesNotExist:
            messages.error(self.request, 'O mecânico não existe!')
            reverse_lazy('mecanicos_list')

    def get_context_data(self, **kwargs):
        context = super(MecanicoUpdateView, self).get_context_data(**kwargs)
        context['mecanico'] = self.get_mecanico(self.kwargs['pk'])
        self.initial['estado'] = context['mecanico'].pessoa.endereco.estado # BUG
        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        especialidade = form.cleaned_data['especialidade']

        cep = form.cleaned_data['cep']
        rua = form.cleaned_data['rua']
        bairro = form.cleaned_data['bairro']
        numero = form.cleaned_data['numero']
        complemento = form.cleaned_data['complemento']
        cidade = form.cleaned_data['cidade']
        estado = form.cleaned_data['estado']

        mecanico = self.get_context_data()['mecanico']
        endereco = mecanico.pessoa.endereco

        endereco.cep = cep
        endereco.rua = rua
        endereco.bairro = bairro
        endereco.numero = numero
        endereco.complemento = complemento
        endereco.cidade = cidade
        endereco.estado = estado
        endereco.save()

        pessoa = mecanico.pessoa
        pessoa.nome = nome
        pessoa.save()

        mecanico.especialidade = especialidade
        mecanico.pessoa = pessoa
        mecanico.save()

        messages.success(self.request, 'Mecânico atualizado.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar o mecânico.')
        print(form.errors)
        return super().form_invalid(form)


class MecanicoDeleteView(DeleteView):
    model = Mecanico
    template_name = 'mecanico/delete.html'
    success_url = reverse_lazy("mecanicos_list")


class EquipeListView(ListView):

    model = Equipe
    context_object_name = 'equipes'
    ordering = ['-id']
    template_name = 'equipes/list.html'
    paginate_by = 10


class EquipeCreateView(FormView):
    form_class = EquipeForm
    template_name = 'equipes/create.html'
    success_url = '/equipes/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Equipe adicionada.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar a equipe.')
        return super().form_invalid(form)


class EquipeUpdateView(UpdateView):
    model = Equipe
    form_class = EquipeForm
    template_name = 'equipes/edit.html'
    success_url = reverse_lazy("equipes_list")
    slug_field = 'pk'
    slug_url_kwarg = 'pk'


class EquipeDeleteView(DeleteView):
    model = Equipe
    template_name = 'equipes/delete.html'
    success_url = reverse_lazy("equipes_list")
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
