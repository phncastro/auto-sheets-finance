from dataclasses import dataclass

@dataclass
class Notificacao:

    app: str
    titulo: str
    texto: str