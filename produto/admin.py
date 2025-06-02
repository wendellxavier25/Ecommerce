from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutosAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto', 'nome']
