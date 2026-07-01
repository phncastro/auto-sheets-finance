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

import re

class BradescoParser:
    
    def __init__(self, tipo, valor, descricao, banco):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.banco = banco

    def identificar_tipo(self, transação):

        regex_tipo_credito = r"COMPRA\s+APROVADA"
        regex_tipo_pix_enviado = r"Você\s+enviou\s+um\s+Pix"
        regex_tipo_pix_recebido = r"Você\s+recebeu\s+um\s+Pix"
        
        if re.search(regex_tipo_credito, transação):
            return 'CRÉDITO'
        elif re.search(regex_tipo_pix_enviado, transação):
            return 'PIX ENVIADO'
        elif re.search(regex_tipo_pix_recebido, transação):
            return 'PIX RECEBIDO'

        return 'Error: Tipo não identificado'


    def realizar_parse(self, transação):

        regex_valor_credito = r"VALOR\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
        regex_estabelecimento = r"VALOR\s+R\$\s*\d+(?:\.\d{3})*,\d{2}\s*(.*?)\s*LIMITE\s+DISP"
        regex_valor_pix = r"Pix\s+de\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
        regex_destinatario_pix = r"para\s+a\s+conta\s+de\s+(.*?),\s+na\s+Instituição"
        regex_remetente_pix = r"para\s+a\s+conta\s+de\s+(.*?),\s+da\s+instituição"

        self.tipo = self.identificar_tipo()

        if self.tipo == 'CRÉDITO':
            self.valor = re.search(regex_valor_credito, transação).group()              # /// TRATAR None
            self.descricao = re.search(regex_estabelecimento, transação).group()        # /// TRATAR None
            self.banco = 'Bradesco'

        elif self.tipo == 'PIX ENVIADO':
            self.valor = re.search(regex_valor_pix, transação).group()                  # /// TRATAR None
            self.descricao = re.search(regex_destinatario_pix, transação).group()       # /// TRATAR None
            self.banco = 'Bradesco'

        elif self.tipo == 'PIX RECEBIDO':
            self.valor = re.search(regex_valor_pix, transação).group()                  # /// TRATAR None
            self.descricao = re.search(regex_remetente_pix, transação).group()          # /// TRATAR None
            self.banco = 'Bradesco'

        return  {
            'tipo': self.tipo,
            'valor': self.valor,
            'descricao': self.descricao,
            'banco': self.banco
        }

