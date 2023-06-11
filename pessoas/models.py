from django.db import models


class Endereco(models.Model):

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    estados = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    cep = models.IntegerField()
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2, choices=estados, default='RO')

    def __str__(self):
        return f'{self.rua} ({self.numero}), {self.cidade} - {self.estado}'


class Pessoa(models.Model):

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cliente(models.Model):

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.pessoa} ({self.telefone})'


class Mecanico(models.Model):

    class Meta:
        verbose_name = 'Mecânico'
        verbose_name_plural = 'Mecânicos'

    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True)
    especialidade = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pessoa} ({self.especialidade})'


class Equipe(models.Model):

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    descricao = models.CharField(max_length=255)
    mecanicos = models.ManyToManyField(Mecanico)

    def __str__(self):
        return self.descricao
