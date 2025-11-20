# mensagens/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    # Ajuste os campos conforme o seu modelo
    list_display = ['nome', 'email', 'servico', 'status_badge', 'created_at']
    list_filter = ['servico', 'created_at']
    search_fields = ['nome', 'email', 'mensagem']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('nome', 'email', 'telefone'),
            'classes': ('wide',),
        }),
        ('Detalhes da Solicitação', {
            'fields': ('servico', 'mensagem'),
            'classes': ('wide',),
        }),
        ('Informações do Sistema', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    
    def status_badge(self, obj):
        """Adiciona badge de status visual"""
        return format_html(
            '<span style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); '
            'color: white; padding: 6px 14px; border-radius: 8px; font-weight: 600; '
            'font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; '
            'box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);">'
            '📩 Nova</span>'
        )
    status_badge.short_description = 'Status'
    
    def has_delete_permission(self, request, obj=None):
        """Permite deletar mensagens"""
        return True
    
    def has_add_permission(self, request):
        """Desabilita adição manual pelo admin"""
        return False
    
    class Media:
        css = {
            'all': ('css/jazzmin_custom.css',)
        }

# Customização adicional do site admin
admin.site.site_header = "Horizon Global Consulting"
admin.site.site_title = "Horizon Admin"
admin.site.index_title = "Painel de Controle"