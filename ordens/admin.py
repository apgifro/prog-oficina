from django.contrib import admin

from ordens.models import Item, Servico, Peca, Veiculo, OrdemDeServico


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'preco']
    search_fields = ['descricao']
    search_help_text = "Digite o nome do item para pesquisar"


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['item']
    search_fields = ['item__descricao']
    search_help_text = "Digite a descrição do item para pesquisar"


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ['item']
    search_fields = ['item__descricao']
    search_help_text = "Digite a descrição do item para pesquisar"


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'descricao', 'cliente', 'equipe']
    search_fields = ['placa', 'descricao', 'cliente__pessoa__nome']
    search_help_text = "Digite a placa, descrição do veículo ou nome do cliente para pesquisar"


@admin.register(OrdemDeServico)
class OrdemDeServicoAdmin(admin.ModelAdmin):
    list_display = ['emitida', 'veiculo', 'entrega', 'total']
    search_fields = ['veiculo__placa', 'emitida']
    search_help_text = "Digite a placa do veículo ou data da ordem de serviço para pesquisar"
