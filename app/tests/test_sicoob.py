from app.parsers.sicoob import SicoobParser

def test_credito():

    notificacao = """Sicoobcard informa: compra crédito aprovada com seu cartão
        Visa final 9920 em 16/09 ás 07:21, valor R$10,00. 
        Local: SPOTIFY"""

    parser = SicoobParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == '10,00'
    assert transacao.tipo.value == 'CRÉDITO'
    assert transacao.descricao == 'SPOTIFY'

def test_debito():

    notificacao = """Sicoobcard informa: compra débito aprovada com seu cartão
        Visa final 9920 em 16/09 ás 07:21, valor R$10,00. 
        Local: SPOTIFY"""

    parser = SicoobParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == '10,00'
    assert transacao.tipo.value == 'DÉBITO'
    assert transacao.descricao == 'SPOTIFY'

def test_pix_enviado():

    notificacao = """Pix de R$500,00 foi enviado para João da Silva, 
        CPF ***.999.111-**."""

    parser = SicoobParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == '500,00'
    assert transacao.tipo.value == 'PIX ENVIADO'
    assert transacao.descricao == 'João da Silva'

def test_pix_recebido():

    notificacao = """Pix de R$500,00 foi recebido de João da Silva, 
        CPF ***.999.111-**."""

    parser = SicoobParser()
    transacao = parser.realizar_parse(notificacao)

    assert transacao.valor == '500,00'
    assert transacao.tipo.value == 'PIX RECEBIDO'
    assert transacao.descricao == 'João da Silva'