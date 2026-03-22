from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")

    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    TIPOS = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movimentacoes')

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} ({self.quantidade})"

    def save(self, *args, **kwargs):
        produto = self.produto

    # 🧠 Se for UPDATE (já existe)
        if self.pk:
            antiga = Movimentacao.objects.get(pk=self.pk)

            # 🔄 Reverte valor antigo
            if antiga.tipo == 'entrada':
                produto.quantidade -= antiga.quantidade
            elif antiga.tipo == 'saida':
                produto.quantidade += antiga.quantidade

            # 🚀 Aplica novo valor
        if self.tipo == 'entrada':
            produto.quantidade += self.quantidade

        elif self.tipo == 'saida':
            if produto.quantidade < self.quantidade:
                raise ValueError("Estoque insuficiente")

            produto.quantidade -= self.quantidade

        produto.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        produto = self.produto

        if self.tipo == 'entrada':
            # reverte a entrada → tira do estoque
            if produto.quantidade < self.quantidade:
                raise ValueError("Erro ao excluir: estoque inconsistente")

            produto.quantidade -= self.quantidade

        elif self.tipo == 'saida':
            # reverte a saída → devolve ao estoque
            produto.quantidade += self.quantidade

        produto.save()

        super().delete(*args, **kwargs)
