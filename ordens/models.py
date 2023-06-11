from django.db import models

from pessoas.models import Cliente, Equipe


class Item(models.Model):

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    descricao = models.CharField(max_length=255)
    preco = models.FloatField()

    def __str__(self):
        return f'{self.descricao}, R$ {self.preco}'


class Servico(models.Model):

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.item} (Serviço)'


class Peca(models.Model):

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'

    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.item} (Peça)'


class Veiculo(models.Model):

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    placa = models.CharField(max_length=7, primary_key=True)
    descricao = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.placa}: {self.descricao} de {self.cliente.pessoa.nome}, {self.equipe}'


class OrdemDeServico(models.Model):

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'

    emitida = models.DateTimeField(auto_now_add=True)
    entrega = models.DateTimeField()
    itens = models.ManyToManyField(Item)
    total = models.FloatField()
    veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.entrega}, {self.veiculo}'
