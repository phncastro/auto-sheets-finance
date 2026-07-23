from decimal import Decimal

def to_decimal(valor: str) -> Decimal:

    return Decimal(
        valor
        .replace('.','')
        .replace(',', '.')
    )

def to_real(valor: Decimal) -> str:

    valor_str = str(valor)

    return valor_str.replace(
        '.', ','
    )

def parse_money(valor: str) -> str:

    decimal = to_decimal(valor)
    
    return to_real(decimal)