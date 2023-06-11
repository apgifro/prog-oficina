from django.contrib import admin

from pessoas.models import Endereco, Pessoa, Cliente, Mecanico, Equipe


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'cidade', 'estado', 'cep']


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'telefone']


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'especialidade']


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['descricao']
