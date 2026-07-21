from decimal import Decimal

def parse_money(valor: str) -> Decimal:

    return Decimal(
        valor
        .replace('.','')
        .replace(',', '.')
    )