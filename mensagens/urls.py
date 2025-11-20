# mensagens/urls.py
# mensagens/urls.py
from django.urls import path
from .views import Send_message

urlpatterns = [
path ('mensagens/enviar/', Send_message, name='enviar-mensagem'),

]