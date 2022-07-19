from django.contrib import admin
from api.models import cliente,produto, pedido
# Register your models here.
class clientes(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','telefone')
    list_display_links = ('id','nome','sobrenome','email','telefone')
    search_fields = ['nome']
admin.site.register(cliente,clientes)
#tabela produto

class produtos(admin.ModelAdmin):
    list_display = ('id','nome_do_produto','marca','quantidade')
    list_display_links = ('id','nome_do_produto','marca','quantidade')
    search_fields = ['nome_do_produto']
admin.site.register(produto,produtos) 

class pedidos(admin.ModelAdmin):
    list_display = ('id','dados_do_pedido','produto','quantidades','dados_do_cliente')
    list_display_links = ('id','dados_do_pedido','produto','quantidades','dados_do_cliente')
    search_fields = ['dados_do_pedido']
admin.site.register(pedido,pedidos) 