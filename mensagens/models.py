# mensagens/models.py
from django.db import models
from django.utils import timezone

class Mensagem(models.Model):
    SERVICOS_CHOICES = [
        ('Contabilidade', 'Contabilidade'),
        ('Consultoria Fiscal', 'Consultoria Fiscal'),
        ('Consultoria Financeira', 'Consultoria Financeira'),
        ('Auditoria', 'Auditoria'),
        ('Consultoria de Gestão Empresarial', 'Consultoria de Gestão Empresarial'),
        ('Controlo de Gestão', 'Controlo de Gestão'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Serviços Administrativos', 'Serviços Administrativos'),
        ('Faturação', 'Faturação'),
        ('Outro', 'Outro'),
    ]
    
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    servico = models.CharField(max_length=100, choices=SERVICOS_CHOICES, verbose_name="Serviço")
    mensagem = models.TextField(verbose_name="Mensagem")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Data de Envio")
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.nome} - {self.servico}"