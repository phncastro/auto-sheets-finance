from app.parsers.bradesco import BradescoParser
from decimal import Decimal

def test_credito():

    notificacao = """BRADESCO CARTOES: COMPRA APROVADA CARTAO FINAL 8224 EM 29/06/2026 20:16, VALOR R$ 54,99 CONVENIENCIA   SÃO PAULO LIMITE DISP R$ 2883,04"""

    parser = BradescoParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == Decimal('54.99')
    assert transacao.tipo.value == 'CRÉDITO'
    assert transacao.descricao == 'CONVENIENCIA'

def test_pix_enviado():

    notificacao = """Você enviou um Pix de R$ 400,00 para a conta de JOÃO DA SILVA, na Instituição CAIXA ECONOMICA FEDERAL"""

    parser = BradescoParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == Decimal('400.00')
    assert transacao.tipo.value == 'PIX ENVIADO'
    assert transacao.descricao == 'JOÃO DA SILVA'

def test_pix_recebido():

    notificacao = """Você recebeu um Pix de R$ 600,00 de JOÃO DA SILVA, da instituição CAIXA ECONOMICA FEDERAL"""

    parser = BradescoParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == Decimal('600.00')
    assert transacao.tipo.value == 'PIX RECEBIDO'
    assert transacao.descricao == 'JOÃO DA SILVA'