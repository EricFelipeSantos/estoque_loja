from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, CategoriaViewSet, MovimentacaoViewSet

app_name = 'estoque'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.criar_produto, name='produto_create'),
    path('<int:pk>/editar/', views.editar_produto, name='produto_update'),
    path('<int:pk>/excluir/', views.excluir_produto, name='produto_delete'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nova/', views.criar_categoria, name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='categoria_update'),
    path('categorias/<int:pk>/excluir/', views.excluir_categoria, name='categoria_delete'),

    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/nova/', views.criar_movimentacao, name='movimentacao_create'),
    path('movimentacoes/<int:pk>/excluir/', views.excluir_movimentacao, name='movimentacao_delete'),
]

router = DefaultRouter()
router.register(r'produto', ProdutoViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'movimentacao', MovimentacaoViewSet)

urlpatterns += router.urls