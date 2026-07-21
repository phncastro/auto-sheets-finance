import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.services.transaction_service import TransactionService
from app.services.sheets_service import GoogleSheetsService
from app.core.notification import Notificacao

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
        google_service = GoogleSheetsService()
        google_service.adicionar(transacao)

        return JsonResponse({
            "status": "ok"
        })

    return JsonResponse({"erro": "metodo inválido"})

def index(request):
    return 'Olá mundo'
