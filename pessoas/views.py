from django.shortcuts import render

from django.views.generic.list import ListView

from pessoas.models import Cliente, Mecanico, Equipe


class ClienteListView(ListView):

    model = Cliente
    ordering = ['-pessoa_id']
    context_object_name = 'clientes'
    template_name = 'cliente/list.html'
    paginate_by = 20


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

