def extrair(regex: str, transacao: str) -> str | None:

    import re

    match = re.search(regex, transacao, re.IGNORECASE)

    if match is None:
        return None

    if match.lastindex:
        return match.group(1)
    
    return match.group()