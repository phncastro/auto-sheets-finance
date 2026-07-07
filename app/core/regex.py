def extrair(regex: str, transacao: str) -> str:

    import re

    match = re.search(regex, transacao)

    if match is None:
        raise ValueError(
            f"Regex '{regex}' não encontrou correspondência."
        )

    return match.group(1)