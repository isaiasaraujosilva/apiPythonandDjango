from django.contrib import admin
from api.models import cliente,produto
# Register your models here.
class clientes(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','telefone')
    list_display_links = ('id','nome','sobrenome','email','telefone')
    search_fields = ['nome']
admin.site.register(cliente,clientes)
#tabela produto

class produtos(admin.ModelAdmin):
    list_display = ('id','nome_do_produto','marca','unidade')
    list_display_links = ('id','nome_do_produto','marca','unidade')
    search_fields = ['nome']
admin.site.register(produto,produtos) 