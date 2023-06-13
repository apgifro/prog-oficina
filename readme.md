# Oficina

## Sobre

Prova de Programação realizada em Python / Django.

## Imagens

![](/readme/1.png)

![](/readme/2.png)

![](/readme/3.png)

![](/readme/4.png)

![](/readme/5.png)

## Desenvolver

1. Clone o projeto
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`
6. Faça um commit e um pull request

Observação: não envie os arquivos de `migrations`, `.idea/` ou `db.sqlite`


## Tarefas

### Admin

- [x] Criar projeto e apps
- [x] Desenvolver `models.py` 
- [x] Adicionar no `admin.py`
- [x] Adicionar funções como `search_fields` no `admin.py`
- [ ] Ajustes finos, como nome, do `admin.py`

### Views, urls e templates

- [x] Ajustar `settings.py` para templates e arquivos estáticos
- [x] Adicionar `bootstrap`
- [x] Criar uma página `index.html` com base em algum modelo `bootstrap`

#### Cliente

- [x] Exibir Cliente
- [x] Criar Cliente
- [x] Atualizar Cliente
- [x] Excluir Cliente

#### Mecânico

- [x] Exibir Mecânico
- [ ] Criar Mecânico
- [ ] Atualizar Mecânico
- [ ] Excluir Mecânico

#### Equipe

- [x] Exibir Equipe
- [ ] Criar Equipe
- [ ] Atualizar Equipe
- [ ] Excluir Equipe

#### Peças

- [x] Exibir Peças
- [x] Criar Peças
- [x] Atualizar Peças
- [x] Excluir Peças

#### Serviços

- [x] Exibir Serviços
- [x] Criar Serviços
- [x] Atualizar Serviços
- [x] Excluir Serviços

#### Veículos

- [x] Exibir Veículos
- [x] Criar Veículos
- [x] Atualizar Veículos
- [x] Excluir Veículos

#### Ordem de Serviço

- [x] Exibir Ordem de Serviço
- [ ] Criar Ordem de Serviço
- [ ] Atualizar Ordem de Serviço
- [ ] Excluir Ordem de Serviço

### Completo

- [ ] Projeto completo!

## Negócio

Para o negócio da oficina se digitalizar, o seguinte fluxo deve ser seguido.

### Um

`Item -> Serviço -> Peça -> Pessoa -> Mecânico -> Equipe`

Deve-se cadastrar os serviços oferecidos, as peças disponíveis, os mecânicos e as equipes de mecânicos.

### Dois

`Pessoa -> Cliente -> Veículo > Ordem de Serviço`

Quando um cliente chegar na oficina, ele será cadastrado assim como o seu veículo.

O veículo estará associado a uma equipe de mecânicos.

Após ouvir a demanda do cliente, será criada uma ordem de serviço com serviços e peças necessárias mais o preço.

