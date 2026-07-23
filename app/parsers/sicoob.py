from app.core.transaction import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposSicoob, RegexDadosSicoob
from app.utils.regex import extrair
from app.utils.money import parse_money

class SicoobParser:

    def identificar_tipo(self, transacao) -> TipoTransacao:
        
        if extrair(
            RegexTiposSicoob.CREDITO.value,
            transacao
            ):
            return TipoTransacao.CREDITO
        
        elif extrair(
            RegexTiposSicoob.DEBITO.value,
            transacao
            ):
            return TipoTransacao.DEBITO
        
        elif extrair(
            RegexTiposSicoob.PIX_ENVIADO.value,
            transacao
            ):
            return TipoTransacao.PIX_ENVIADO
        
        elif extrair(
            RegexTiposSicoob.PIX_RECEBIDO.value,
            transacao
            ):
            return TipoTransacao.PIX_RECEBIDO

        return None
    

    def realizar_parse(self, transacao) -> Transacao:

        tipo = self.identificar_tipo(transacao)
        banco = Banco.SICOOB

        if tipo == TipoTransacao.CREDITO:
            valor = extrair(RegexDadosSicoob.VALOR_CARTAO.value, transacao)
            descricao = extrair(RegexDadosSicoob.ESTABELECIMENTO.value, transacao)

        elif tipo == TipoTransacao.DEBITO:
            valor = extrair(RegexDadosSicoob.VALOR_CARTAO.value, transacao)
            descricao = extrair(RegexDadosSicoob.ESTABELECIMENTO.value, transacao)

        elif tipo == TipoTransacao.PIX_ENVIADO:
            valor = extrair(RegexDadosSicoob.VALOR_PIX.value, transacao)
            descricao = extrair(RegexDadosSicoob.DESTINATARIO.value, transacao)

        elif tipo == TipoTransacao.PIX_RECEBIDO:
            valor = extrair(RegexDadosSicoob.VALOR_PIX.value, transacao)
            descricao = extrair(RegexDadosSicoob.REMETENTE.value, transacao)

        else:
            return None
                
        return Transacao(
            banco,
            tipo,
            parse_money(valor),
            descricao.upper()
        )
