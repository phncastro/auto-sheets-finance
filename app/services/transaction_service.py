from app.parsers.bradesco import BradescoParser
from app.parsers.sicoob import SicoobParser

class TransactionService:

    def processar(notificacao):

        PARSERS = {
            'Sicoob': SicoobParser(),
            'Bradesco': BradescoParser(),
            'Mensagens': BradescoParser(),
        }

        parser = PARSERS.get(notificacao.app)

        if parser is None:
            return None
        
        return parser.realizar_parse(notificacao.texto)