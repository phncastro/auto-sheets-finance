# O BANCO É RESPONSÁVEL SOMENTE POR REALIZAR OS MÉTODOS E O PARSE CORRETO DA NOTIFICAÇÃO

'''
    EX DE NOTIFICAÇÕES: 

    // COMPRA CRÉDITO - APP SICOOBCARD

    Sicoobcard informa: compra crédito aprovada com seu cartão
    Visa final 9920 em 16/09 ás 07:21, valor R$10,00. 
    Local: SPOTIFY

    // COMPRA CRÉDITO - APP SICOOBCARD

    Sicoobcard informa: compra débito aprovada com seu cartão
    Visa final 9920 em 16/09 ás 07:21, valor R$10,00. 
    Local: SPOTIFY
    
    // PIX ENVIADO - APP SICOOB
    
    Pix de R$500,00 foi enviado para João da Silva, 
    CPF ***.999.111-**.

    // PIX RECEBIDO - APP SICOOB

    Pix de R$500,00 foi recebido de João da Silva, 
    CPF ***.999.111-**.


'''

from app.models import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposSicoob, RegexDadosSicoob
import re

class SicoobParser:
    
    def __init__(self, tipo, valor, descricao, banco):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.banco = banco

    def identificar_tipo(self, transação):
        
        if re.search(RegexTiposSicoob.CREDITO, transação):
            return TipoTransacao.CREDITO
        elif re.search(RegexTiposSicoob.DEBITO, transação):
            return TipoTransacao.DEBITO
        elif re.search(RegexTiposSicoob.PIX_ENVIADO, transação):
            return TipoTransacao.PIX_ENVIADO
        elif re.search(RegexTiposSicoob.PIX_RECEBIDO, transação):
            return TipoTransacao.PIX_RECEBIDO

        return 'Error: Tipo não identificado'                                          # /// TRATAR NOTIFICAÇÕES DIFERENTES
    

    def realizar_parse(self, transação):

        self.tipo = self.identificar_tipo()

        if self.tipo == TipoTransacao.CREDITO:
            self.valor = re.search(RegexDadosSicoob.VALOR_CARTAO, transação).group()                      # /// TRATAR None
            self.descricao = re.search(RegexDadosSicoob.ESTABELECIMENTO, transação).group()        # /// TRATAR None
            self.banco = Banco.SICOOB

        elif self.tipo == TipoTransacao.DEBITO:
            self.valor = re.search(RegexDadosSicoob.VALOR_CARTAO, transação).group()                      # /// TRATAR None
            self.descricao = re.search(RegexDadosSicoob.ESTABELECIMENTO, transação).group()        # /// TRATAR None
            self.banco = Banco.SICOOB

        elif self.tipo == TipoTransacao.PIX_ENVIADO:
            self.valor = re.search(RegexDadosSicoob.VALOR_PIX, transação).group()                  # /// TRATAR None
            self.descricao = re.search(RegexDadosSicoob.DESTINATARIO, transação).group()           # /// TRATAR None
            self.banco = Banco.SICOOB

        elif self.tipo == TipoTransacao.PIX_RECEBIDO:
            self.valor = re.search(RegexDadosSicoob.VALOR_PIX, transação).group()                  # /// TRATAR None
            self.descricao = re.search(RegexDadosSicoob.REMETENTE, transação).group()              # /// TRATAR None
            self.banco = Banco.SICOOB

        transacao = Transacao(self.tipo, self.valor, self.descricao, self.banco)
                
        return transacao

  