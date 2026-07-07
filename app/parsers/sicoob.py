from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposSicoob, RegexDadosSicoob
import re

class SicoobParser:

    def identificar_tipo(self, transação):
        
        if re.search(RegexTiposSicoob.CREDITO.value, transação):
            return TipoTransacao.CREDITO
        elif re.search(RegexTiposSicoob.DEBITO.value, transação):
            return TipoTransacao.DEBITO
        elif re.search(RegexTiposSicoob.PIX_ENVIADO.value, transação):
            return TipoTransacao.PIX_ENVIADO
        elif re.search(RegexTiposSicoob.PIX_RECEBIDO.value, transação):
            return TipoTransacao.PIX_RECEBIDO

        return None
    

    def realizar_parse(self, transação):

        tipo = self.identificar_tipo(transação)

        if tipo == TipoTransacao.CREDITO:
            valor = re.search(RegexDadosSicoob.VALOR_CARTAO.value, transação).group(1)               # /// TRATAR None
            descricao = re.search(RegexDadosSicoob.ESTABELECIMENTO.value, transação).group(1)        # /// TRATAR None
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.DEBITO:
            valor = re.search(RegexDadosSicoob.VALOR_CARTAO.value, transação).group(1)               # /// TRATAR None
            descricao = re.search(RegexDadosSicoob.ESTABELECIMENTO.value, transação).group(1)        # /// TRATAR None
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.PIX_ENVIADO:
            valor = re.search(RegexDadosSicoob.VALOR_PIX.value, transação).group(1)                  # /// TRATAR None
            descricao = re.search(RegexDadosSicoob.DESTINATARIO.value, transação).group(1)           # /// TRATAR None
            banco = Banco.SICOOB

        elif tipo == TipoTransacao.PIX_RECEBIDO:
            valor = re.search(RegexDadosSicoob.VALOR_PIX.value, transação).group(1)                  # /// TRATAR None
            descricao = re.search(RegexDadosSicoob.REMETENTE.value, transação).group(1)              # /// TRATAR None
            banco = Banco.SICOOB

        else:
            return None
                
        return Transacao(
            tipo,
            valor,
            descricao,
            banco
        )

  