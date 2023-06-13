# Oficina

## Sobre

Prova de Programação realizada em Python e Django.
Alexandre e Makalister.

## Imagens

![](/readme/1.png)

![](/readme/10.png)

![](/readme/2.png)

![](/readme/3.png)

![](/readme/4.png)

![](/readme/5.png)

![](/readme/6.png)

![](/readme/7.png)

![](/readme/8.png)

![](/readme/9.png)

![](/readme/11.png)

![](/readme/12.png)

## Tarefas

### Admin

- [x] Criar projeto e apps
- [x] Desenvolver `models.py` 
- [x] Adicionar no `admin.py`
- [x] Adicionar funções como `search_fields` no `admin.py`

### Views, urls e templates

- [x] Ajustar `settings.py` para templates e arquivos estáticos
- [x] Adicionar `bootstrap`
- [x] Criar uma página `index.html` com base em algum modelo `bootstrap`

#### Views

- [x] Exibir, criar, atualizar e excluir `Cliente`
- [x] Exibir, criar, atualizar e excluir `Mecânico`
- [x] Exibir, criar, atualizar e excluir `Peças`
- [x] Exibir, criar, atualizar e excluir `Serviços`
- [x] Exibir, criar, atualizar e excluir `Veículos`
- [x] Exibir, criar, atualizar e excluir `Equipes`
- [x] Exibir, criar, atualizar e excluir `Ordens de Serviço`

### Usuários

- [x] Implementar usuários e gerentes

### Completo

- [x] Projeto completo!

## Negócio

Para o negócio da oficina se digitalizar, o seguinte fluxo deve ser seguido.

### Um

`Item : Serviço : Peça : Pessoa : Mecânico : Equipe`

Deve-se cadastrar os serviços oferecidos, as peças disponíveis, os mecânicos e as equipes de mecânicos.

### Dois

`Pessoa : Cliente : Veículo > Ordem de Serviço`

Quando um cliente chegar na oficina, ele será cadastrado assim como o seu veículo.

O veículo estará associado a uma equipe de mecânicos.

Após ouvir a demanda do cliente, será criada uma ordem de serviço com serviços e peças necessárias mais o preço.
