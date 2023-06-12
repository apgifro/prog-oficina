from django.contrib import admin
from pessoas.models import Endereco, Pessoa, Cliente, Mecanico, Equipe


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'cidade', 'estado', 'cep']
    search_fields = ['rua', 'cidade', 'cep']
    search_help_text = "Digite o nome da rua, cidade ou CEP para pesquisar"


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco']
    search_fields = ['nome', 'endereco__rua', 'endereco__cidade', 'endereco__cep']
    search_help_text = "Digite o nome da pessoa ou endereço para pesquisar"


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'telefone']
    search_fields = ['pessoa__nome']
    search_help_text = "Digite o nome do cliente para pesquisar"


@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'especialidade']
    search_fields = ['pessoa__nome', 'especialidade']
    search_help_text = "Digite a especialidade ou nome do mecânico para pesquisar"


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['descricao']
    search_fields = ['descricao']
    search_help_text = "Digite a descrição da equipe para pesquisar"
