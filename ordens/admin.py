from django.contrib import admin

from ordens.models import Item, Servico, Peca, Veiculo, OrdemDeServico


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'preco']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['item']


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ['item']


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'descricao', 'cliente', 'equipe']


@admin.register(OrdemDeServico)
class OrdemDeServicoAdmin(admin.ModelAdmin):
    list_display = ['emitida', 'veiculo', 'entrega', 'total']
    search_fields = ['veiculo__cliente__pessoa__nome']
