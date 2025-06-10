from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutosAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]
    list_display = ['nome', 'descricao_curta', 'preco_marketing', 'preco_marketing_promocional']

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto', 'nome']
