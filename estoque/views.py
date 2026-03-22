from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria, Movimentacao
from .forms import ProdutoForm, CategoriaForm, MovimentacaoForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProdutoSerializer, CategoriaSerializer, MovimentacaoSerializer
from django.db.models.deletion import ProtectedError
from django.contrib import messages


# =========================
# 📦 PRODUTOS
# =========================

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/produto_list.html', {'produtos': produtos})


@login_required(login_url='core:login')
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'estoque/produto_form.html', {'form': form})


@login_required(login_url='core:login')
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'estoque/produto_form.html', {'form': form})


@login_required(login_url='core:login')
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        produto.delete()
        return redirect('estoque:lista_produtos')

    return render(request, 'estoque/produto_confirm_delete.html', {'produto': produto})


# =========================
# 🗂️ CATEGORIAS
# =========================

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'estoque/categoria_list.html', {'categorias': categorias})


@login_required(login_url='core:login')
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_categorias')
    else:
        form = CategoriaForm()

    return render(request, 'estoque/categoria_form.html', {'form': form})


@login_required(login_url='core:login')
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('estoque:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'estoque/categoria_form.html', {'form': form})


@login_required(login_url='core:login')
def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir categoria com produtos vinculados.")

        return redirect('estoque:lista_categorias')

    return render(request, 'estoque/categoria_confirm_delete.html', {'categoria': categoria})


# =========================
# 🔄 MOVIMENTAÇÕES
# =========================

def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all().order_by('-data')
    return render(request, 'estoque/movimentacao_list.html', {'movimentacoes': movimentacoes})


@login_required(login_url='core:login')
def criar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.usuario = request.user

            try:
                movimentacao.save()
                return redirect('estoque:lista_movimentacoes')
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = MovimentacaoForm()

    return render(request, 'estoque/movimentacao_form.html', {'form': form})


@login_required(login_url='core:login')
def excluir_movimentacao(request, pk):
    movimentacao = get_object_or_404(Movimentacao, pk=pk)

    if request.method == 'POST':
        movimentacao.delete()
        return redirect('estoque:lista_movimentacoes')

    return render(request, 'estoque/movimentacao_confirm_delete.html', {'movimentacao': movimentacao})


# =========================
# 🔌 API REST
# =========================

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]


class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
    permission_classes = [IsAuthenticated]