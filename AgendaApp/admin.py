from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone, Interesse


# Register your models here.

class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1


class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'email', 'endereco']
    list_display_links = ['id', 'nome']
    list_filter = ['id', 'nome', 'apelido']
    search_fields = ['nome', 'id', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']


admin.site.register(Contato, ContatoAdmin)    
admin.site.register(Cidade)  
admin.site.register(Telefone)  
admin.site.register(Interesse)  