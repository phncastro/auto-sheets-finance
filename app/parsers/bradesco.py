from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposBradesco, RegexDadosBradesco
from app.core.regex import extrair

class BradescoParser:

    def identificar_tipo(self, transacao) -> TipoTransacao:
        
        if extrair(
            RegexTiposBradesco.CREDITO.value,
            transacao
            ):
            return TipoTransacao.CREDITO
        
        elif extrair(
            RegexTiposBradesco.PIX_ENVIADO.value,
            transacao
            ):
           return TipoTransacao.PIX_ENVIADO
        
        elif extrair(
            RegexTiposBradesco.PIX_RECEBIDO.value,
            transacao
            ):
            return TipoTransacao.PIX_RECEBIDO

        return None


    def realizar_parse(self, transacao) -> Transacao:

        tipo = self.identificar_tipo(transacao)

        if tipo == TipoTransacao.CREDITO:

            valor = extrair(RegexDadosBradesco.VALOR_CARTAO.value, transacao)
            descricao = extrair(RegexDadosBradesco.ESTABELECIMENTO.value, transacao)
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_ENVIADO:

            valor = extrair(RegexDadosBradesco.VALOR_PIX.value, transacao)
            descricao = extrair(RegexDadosBradesco.DESTINATARIO.value, transacao)
            banco = Banco.BRADESCO

        elif tipo == TipoTransacao.PIX_RECEBIDO:

            valor = extrair(RegexDadosBradesco.VALOR_PIX.value, transacao)
            descricao = extrair(RegexDadosBradesco.REMETENTE.value, transacao)
            banco = Banco.BRADESCO

        else:
            return None
        
        return Transacao(
            tipo,
            valor,
            descricao,
            banco
        )

