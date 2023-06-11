from django.shortcuts import render, redirect
from pessoas.forms import EnderecoForm, PessoaForm, ClienteForm, MecanicoForm, EquipeForm

def create_endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            endereco = form.save()
            return redirect('endereco_detail', pk=endereco.pk)
    else:
        form = EnderecoForm()
    return render(request, 'pessoas/endereco_create.html', {'form': form})


def create_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            return redirect('pessoa_detail', pk=pessoa.pk)
    else:
        form = PessoaForm()
    return render(request, 'pessoas/pessoa_create.html', {'form': form})


def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_detail', pk=cliente.pessoa.pk)
    else:
        form = ClienteForm()
    return render(request, 'pessoas/cliente_create.html', {'form': form})


def create_mecanico(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            mecanico = form.save()
            return redirect('mecanico_detail', pk=mecanico.pessoa.pk)
    else:
        form = MecanicoForm()
    return render(request, 'pessoas/mecanico_create.html', {'form': form})


def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe = form.save()
            return redirect('equipe_detail', pk=equipe.pk)
    else:
        form = EquipeForm()
    return render(request, 'pessoas/equipe_create.html', {'form': form})
