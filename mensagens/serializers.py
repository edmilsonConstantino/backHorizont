
# mensagens/serializers.py
from rest_framework import serializers
from .models import Mensagem

class MensagemSerializer(serializers.ModelSerializer):
     class Meta:
          model = Mensagem

          fields = [
               'id',
               'nome',
               'apelido',
               'email',
               'telefone',
               'servico',
               'mensagem',
               'data_criacao',
            ]
read_only_fields = ['id', 'data_criacao']