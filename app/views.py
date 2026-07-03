import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Transacao

@csrf_exempt
def receber_transacao(request):
    if request.method == "POST":
        data = json.loads(request.body)

        import re
        regex_valor = r"\s+R\$\s?(\d+(?:\.\d{3})*,\d{2})"
        regex_valor_bradesco = r"VALOR\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"

        titulo = data.get('titulo')
        texto = data.get("texto")

        valor = re.search(regex_valor, texto)
        if valor:
            valor = valor.group(1)
        else:
            valor = None

        app = data.get("app")
        
        transacao = Transacao(
            texto=texto,
            banco=app
            )
        
        transacao.save()

        print("=== NOVA TRANSAÇÃO ===")
        print("Texto:", texto)
        print("Valor:", valor)
        print("Banco:", app)

        return JsonResponse({
            "status": "ok",
            "recebido": data
        })

    return JsonResponse({"erro": "metodo inválido"})

def index(request):
    return 'Olá mundo'
