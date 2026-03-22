from django.contrib import admin
from .models import Produto, Categoria, Movimentacao


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria')
    search_fields = ('nome', 'categoria__nome')
    list_filter = ('categoria',)
    ordering = ('nome',)
    list_per_page = 25


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)
    list_per_page = 25


class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'tipo', 'quantidade', 'data', 'usuario')
    search_fields = ('produto__nome', 'usuario__username')
    list_filter = ('tipo', 'data')
    ordering = ('-data',)
    list_per_page = 25


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Movimentacao, MovimentacaoAdmin)