from django.contrib import admin
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    # Ajuste conforme seu modelo
    list_display = ['nome', 'email', 'servico', 'created_at']
    list_filter = ['servico', 'created_at']
    search_fields = ['nome', 'email', 'mensagem']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('nome', 'email', 'telefone'),
        }),
        ('Detalhes da Solicitação', {
            'fields': ('servico', 'mensagem'),
        }),
        ('Informações do Sistema', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

# Configuração padrão do admin
admin.site.site_header = "Horizon Global Consulting"
admin.site.site_title = "Horizon Admin"
admin.site.index_title = "Painel de Controle"
