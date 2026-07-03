from enum import Enum

class TipoTransacao(Enum):
    CREDITO = 'CRÉDITO'
    DEBITO = 'DÉBITO'
    PIX_ENVIADO = 'PIX ENVIADO'
    PIX_RECEBIDO = 'PIX RECEBIDO'

class Banco(Enum):
    BRADESCO = 'BRADESCO'
    SICOOB = 'SICOOB'