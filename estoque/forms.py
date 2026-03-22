from django.forms import ModelForm
from .models import Produto, Categoria, Movimentacao

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class MovimentacaoForm(ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade']