from django.contrib import admin
from AgendaApp.models import Contato, Cidade


# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'email', 'endereco']
    list_display_links = ['id', 'nome']
    list_filter = ['id', 'nome', 'apelido']
    search_fields = ['nome', 'id', 'apelido']


admin.site.register(Contato, ContatoAdmin)    
admin.site.register(Cidade)  