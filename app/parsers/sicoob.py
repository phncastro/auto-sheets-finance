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

import re

class SicoobParser:
    
    def __init__(self, tipo, valor, descricao, banco):
        self.tipo = tipo
        self.valor = valor
        self.descricao = descricao
        self.banco = banco

    def identificar_tipo(self, transação):

        regex_tipo_credito = r"compra\s+crédito\s+aprovada"
        regex_tipo_debito = r"compra\s+débito\s+aprovada"
        regex_tipo_pix_enviado = r"Pix\s+de\s+R\$.*?foi\s+enviado"
        regex_tipo_pix_recebido = r"Pix\s+de\s+R\$.*?foi\s+recebido"
        
        if re.search(regex_tipo_credito, transação):
            return 'CRÉDITO'
        elif re.search(regex_tipo_debito, transação):
            return 'DÉBITO'
        elif re.search(regex_tipo_pix_enviado, transação):
            return 'PIX ENVIADO'
        elif re.search(regex_tipo_pix_recebido, transação):
            return 'PIX RECEBIDO'

        return 'Error: Tipo não identificado'
    

    def realizar_parse(self, transação):

        regex_valor = r"valor\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
        regex_estabelecimento = r"Local:\s*(.+)"

        regex_valor_pix = r"Pix\s+de\s+R\$\s*(\d+(?:\.\d{3})*,\d{2})"
        regex_destinatario = r"foi\s+enviado\s+para\s+(.+?),\s*CPF"
        regex_remetente = r"foi\s+recebido\s+de\s+(.+?),\s*CPF"

        self.tipo = self.identificar_tipo()

        if self.tipo == 'CRÉDITO':
            self.valor = re.search(regex_valor, transação).group()                      # /// TRATAR None
            self.descricao = re.search(regex_estabelecimento, transação).group()        # /// TRATAR None
            self.banco = 'Sicoob'

        elif self.tipo == 'DÉBITO':
            self.valor = re.search(regex_valor, transação).group()                      # /// TRATAR None
            self.descricao = re.search(regex_estabelecimento, transação).group()        # /// TRATAR None
            self.banco = 'Sicoob'

        elif self.tipo == 'PIX ENVIADO':
            self.valor = re.search(regex_valor_pix, transação).group()                  # /// TRATAR None
            self.descricao = re.search(regex_destinatario, transação).group()           # /// TRATAR None
            self.banco = 'Sicoob'

        elif self.tipo == 'PIX RECEBIDO':
            self.valor = re.search(regex_valor_pix, transação).group()                  # /// TRATAR None
            self.descricao = re.search(regex_remetente, transação).group()              # /// TRATAR None
            self.banco = 'Sicoob'

        return  {
            'tipo': self.tipo,
            'valor': self.valor,
            'descricao': self.descricao,
            'banco': self.banco
        }