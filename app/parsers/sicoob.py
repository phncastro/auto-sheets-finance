from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposSicoob, RegexDadosSicoob
from app.core.regex import extrair
import re

class SicoobParser:

    def identificar_tipo(self, transação):
        
        if extrair(
            RegexTiposSicoob.CREDITO.value,
            transação
            ):
            return TipoTransacao.CREDITO
        
        elif extrair(
            RegexTiposSicoob.DEBITO.value,
            transação
            ):
            return TipoTransacao.DEBITO
        
        elif extrair(
            RegexTiposSicoob.PIX_ENVIADO.value,
            transação
            ):
            return TipoTransacao.PIX_ENVIADO
        
        elif extrair(
            RegexTiposSicoob.PIX_RECEBIDO.value,
            transação
            ):
            return TipoTransacao.PIX_RECEBIDO

        return None
    

    def realizar_parse(self, transação):

        tipo = self.identificar_tipo(transação)

        if tipo == TipoTransacao.CREDITO:
            valor = extrair(RegexDadosSicoob.VALOR_CARTAO.value, transação).group(1)
            descricao = extrair(RegexDadosSicoob.ESTABELECIMENTO.value, transação).group(1)
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.DEBITO:
            valor = extrair(RegexDadosSicoob.VALOR_CARTAO.value, transação).group(1)
            descricao = extrair(RegexDadosSicoob.ESTABELECIMENTO.value, transação).group(1)
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.PIX_ENVIADO:
            valor = extrair(RegexDadosSicoob.VALOR_PIX.value, transação).group(1)
            descricao = extrair(RegexDadosSicoob.DESTINATARIO.value, transação).group(1)
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.PIX_RECEBIDO:
            valor = extrair(RegexDadosSicoob.VALOR_PIX.value, transação).group(1)
            descricao = extrair(RegexDadosSicoob.REMETENTE.value, transação).group(1)
            banco = Banco.SICOOB

        else:
            return None
                
        return Transacao(
            tipo,
            valor,
            descricao,
            banco
        )

  