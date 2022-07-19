from django.contrib import admin
from api.models import cliente
# Register your models here.
class clientes(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','telefone')
    list_display_links = ('id','nome','sobrenome','email','telefone')
    search_fields = ['nome']

admin.site.register(cliente,clientes) 