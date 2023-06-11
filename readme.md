# Oficina

## Sobre

Prova de Programação realizada em Python / Django.

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
- [ ] Adicionar funções como `search_fields` no `admin.py`
- [ ] Ajustes finos, como nome, do `admin.py`

### Views

- [ ] Criar `views.py` para `pessoas`
- [ ] Criar `views.py` para `ordens`

### Templates

- [ ] Ajustar `settings.py` para templates e arquivos estáticos
- [ ] Adicionar `bootstrap`
- [ ] Criar uma página `index.html` com base em algum modelo `bootstrap`
- [ ] Criar `templates` para `pessoas`
- [ ] Criar `templates` para `ordens`

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

