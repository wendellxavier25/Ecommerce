from django.contrib import admin
from .models import Pedido, ItemPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    ...


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    ...
