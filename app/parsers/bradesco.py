from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposBradesco, RegexDadosBradesco
import re

class BradescoParser:

    def identificar_tipo(self, transação) -> TipoTransacao:
        
        if re.search(RegexTiposBradesco.CREDITO.value, transação):
            return TipoTransacao.CREDITO
        elif re.search(RegexTiposBradesco.PIX_ENVIADO.value, transação):
           return TipoTransacao.PIX_ENVIADO
        elif re.search(RegexTiposBradesco.PIX_RECEBIDO.value, transação):
            return TipoTransacao.PIX_RECEBIDO

        return None


    def realizar_parse(self, transação) -> Transacao:

        tipo = self.identificar_tipo(transação)

        if tipo == TipoTransacao.CREDITO:
            valor = re.search(RegexDadosBradesco.VALOR_CARTAO.value, transação).group(1)               # /// TRATAR None
            descricao = re.search(RegexDadosBradesco.ESTABELECIMENTO.value, transação).group(1)        # /// TRATAR None
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_ENVIADO:
            valor = re.search(RegexDadosBradesco.VALOR_PIX.value, transação).group(1)                  # /// TRATAR None
            descricao = re.search(RegexDadosBradesco.DESTINATARIO.value, transação).group(1)           # /// TRATAR None
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_RECEBIDO:
            valor = re.search(RegexDadosBradesco.VALOR_PIX.value, transação).group(1)                  # /// TRATAR None
            descricao = re.search(RegexDadosBradesco.REMETENTE.value, transação).group(1)              # /// TRATAR None
            banco = Banco.BRADESCO

        else:
            return None
        
        return Transacao(
            tipo,
            valor,
            descricao,
            banco
        )

