from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposBradesco, RegexDadosBradesco
from app.core.regex import extrair
import re

class BradescoParser:

    def identificar_tipo(self, transação) -> TipoTransacao:
        
        if extrair(RegexTiposBradesco.CREDITO.value, transação):
            return TipoTransacao.CREDITO
        elif extrair(RegexTiposBradesco.PIX_ENVIADO.value, transação):
           return TipoTransacao.PIX_ENVIADO
        elif extrair(RegexTiposBradesco.PIX_RECEBIDO.value, transação):
            return TipoTransacao.PIX_RECEBIDO

        return None


    def realizar_parse(self, transação) -> Transacao:

        tipo = self.identificar_tipo(transação)

        if tipo == TipoTransacao.CREDITO:
            valor = extrair(RegexDadosBradesco.VALOR_CARTAO.value, transação).group(1)
            descricao = extrair(RegexDadosBradesco.ESTABELECIMENTO.value, transação).group(1)
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_ENVIADO:
            valor = extrair(RegexDadosBradesco.VALOR_PIX.value, transação).group(1)
            descricao = extrair(RegexDadosBradesco.DESTINATARIO.value, transação).group(1)
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_RECEBIDO:
            valor = extrair(RegexDadosBradesco.VALOR_PIX.value, transação).group(1)
            descricao = extrair(RegexDadosBradesco.REMETENTE.value, transação).group(1)
            banco = Banco.BRADESCO

        else:
            return None
        
        return Transacao(
            tipo,
            valor,
            descricao,
            banco
        )

