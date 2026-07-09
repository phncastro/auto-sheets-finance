import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Transacao
from app.services.transaction_service import TransactionService
from app.core.notification import Notificacao
from dataclasses import asdict

@csrf_exempt
def receber_transacao(request):
    if request.method == "POST":
        data = json.loads(request.body)
        notificacao = Notificacao(
            data['app'],
            data['titulo'],
            data['texto']
        )
        transacao = TransactionService.processar(notificacao)

        return JsonResponse({
            "status": "ok",
            "transacao": asdict(transacao)
        })

    return JsonResponse({"erro": "metodo inválido"})

def index(request):
    return 'Olá mundo'
