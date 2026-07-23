from dataclasses import dataclass, field
from app.core.enums import TipoTransacao, Banco
from datetime import date
from decimal import Decimal

@dataclass
class Transacao:
    banco: Banco
    tipo: TipoTransacao
    valor: Decimal
    descricao: str
    data: date = field(default_factory=date.today)

    def linha(self):
        return [
            self.data.strftime("%d/%m/%Y"),
            self.banco.value,
            self.tipo.value,
            str(self.valor),
            self.descricao,
        ]