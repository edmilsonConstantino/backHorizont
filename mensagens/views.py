from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Mensagem

@api_view(['POST'])
def Send_message(request):
    try:
        data = request.data

        Mensagem.objects.create(
            nome=data.get("nome"),
            email=data.get("email"),
            telefone=data.get("telefone"),
            servico=data.get("servico"),
            mensagem=data.get("mensagem"),
        )

        return Response({"message": "Mensagem recebida!"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        print("ERRO:", e)
        return Response({"error": "Erro interno no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
