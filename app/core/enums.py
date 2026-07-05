from enum import Enum

class TipoTransacao(Enum):
    CREDITO = 'CRÉDITO'
    DEBITO = 'DÉBITO'
    PIX_ENVIADO = 'PIX ENVIADO'
    PIX_RECEBIDO = 'PIX RECEBIDO'

class Banco(Enum):
    BRADESCO = 'BRADESCO'
    SICOOB = 'SICOOB'

class RegexTiposSicoob(Enum):
    CREDITO = r"compra\s+crédito\s+aprovada"
    DEBITO = r"compra\s+débito\s+aprovada"
    PIX_ENVIADO = r"Pix\s+de\s+R\$.*?foi\s+enviado"
    PIX_RECEBIDO = r"Pix\s+de\s+R\$.*?foi\s+recebido"

class RegexDadosSicoob(Enum):
    VALOR_CARTAO = r"valor\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
    ESTABELECIMENTO = r"Local:\s*(.+)"
    VALOR_PIX = r"Pix\s+de\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
    DESTINATARIO = r"foi\s+enviado\s+para\s+(.+?),\s*CPF"
    REMETENTE = r"foi\s+recebido\s+de\s+(.+?),\s*CPF"

class RegexTiposBradesco(Enum):
    CREDITO = r"COMPRA\s+APROVADA"
    PIX_ENVIADO = r"Você\s+enviou\s+um\s+Pix"
    PIX_RECEBIDO = r"Você\s+recebeu\s+um\s+Pix"

class RegexDadosBradesco(Enum):
    VALOR_CARTAO = r"VALOR\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
    ESTABELECIMENTO = r"VALOR\s+R\$\s*\d+(?:\.\d{3})*,\d{2}\s*(.*?)\s*LIMITE\s+DISP"
    VALOR_PIX = r"Pix\s+de\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
    DESTINATARIO = r"para\s+a\s+conta\s+de\s+(.*?),\s+na\s+Instituição"
    REMETENTE = r"para\s+a\s+conta\s+de\s+(.*?),\s+da\s+instituição"