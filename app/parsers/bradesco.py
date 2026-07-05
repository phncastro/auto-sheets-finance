# O BANCO É RESPONSÁVEL SOMENTE POR REALIZAR OS MÉTODOS E O PARSE CORRETO DA NOTIFICAÇÃO

'''
    EX DE NOTIFICAÇÕES: 

    // COMPRA CRÉDITO - APP MENSAGENS

    BRADESCO CARTOES: COMPRA APROVADA CARTAO FINAL 8224 EM
    29/06/2026 20:16, VALOR R$ 54,99 CONVENIENCIA
    SÃO PAULO LIMITE DISP R$ 2883,04
    
    // PIX ENVIADO - APP BRADESCO
    
    Você enviou um Pix de R$ 400,00 para a conta de JOÃO
    DA SILVA, na Instituição CAIXA ECONOMICA
    FEDERAL

    // PIX RECEBIDO - APP BRADESCO

    Você recebeu um Pix de R$ 600,00 para a conta de JOÃO
    DA SILVA, da instituição CAIXA ECONOMICA
    FEDERAL
'''
from app.models import Transacao
from app.core.enums import TipoTransacao, Banco, RegexTiposBradesco, RegexDadosBradesco
import re

class BradescoParser:
    
    def __init__(self, tipo, valor, descricao, banco):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.banco = banco

    def identificar_tipo(self, transação) -> TipoTransacao:
        
        if re.search(RegexTiposBradesco.CREDITO, transação):
            return TipoTransacao.CREDITO
        elif re.search(RegexTiposBradesco.PIX_ENVIADO, transação):
            return TipoTransacao.PIX_ENVIADO
        elif re.search(RegexTiposBradesco.PIX_RECEBIDO, transação):
            return TipoTransacao.PIX_RECEBIDO

        return 'Error: Tipo não identificado'                                           # /// TRATAR NOTIFICAÇÕES DIFERENTES


    def realizar_parse(self, transação) -> Transacao:

        self.tipo = self.identificar_tipo(transação)

        if self.tipo == TipoTransacao.CREDITO:
            self.valor = re.search(RegexDadosBradesco.VALOR_CARTAO, transação).group()              # /// TRATAR None
            self.descricao = re.search(RegexDadosBradesco.ESTABELECIMENTO, transação).group()        # /// TRATAR None
            self.banco = Banco.BRADESCO

        elif self.tipo == TipoTransacao.PIX_ENVIADO:
            self.valor = re.search(RegexDadosBradesco.VALOR_PIX, transação).group()                  # /// TRATAR None
            self.descricao = re.search(RegexDadosBradesco.DESTINATARIO, transação).group()       # /// TRATAR None
            self.banco = Banco.BRADESCO

        elif self.tipo == TipoTransacao.PIX_RECEBIDO:
            self.valor = re.search(RegexDadosBradesco.VALOR_PIX, transação).group()                  # /// TRATAR None
            self.descricao = re.search(RegexDadosBradesco.REMETENTE, transação).group()          # /// TRATAR None
            self.banco = Banco.BRADESCO

        transacao = Transacao(self.tipo, self.valor, self.descricao, self.banco)
        
        return transacao

