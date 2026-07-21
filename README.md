# 💰 Auto Sheets Finance

Aplicação desenvolvida em **Python + Django** para automatizar o registro de transações financeiras a partir de notificações do celular.

A aplicação recebe notificações enviadas pelo **Tasker**, identifica automaticamente o banco e o tipo da transação, extrai as informações utilizando **Regex** e registra tudo em uma planilha do **Google Sheets**.

## ✨ Funcionalidades

- 📱 Recebe notificações do Android via HTTP (Tasker)
- 🏦 Suporte para múltiplos bancos
  - Bradesco
  - Sicoob
- 💳 Identificação automática de:
  - Compra no crédito
  - Compra no débito
  - PIX enviado
  - PIX recebido
- 🔎 Extração automática de:
  - Valor
  - Estabelecimento
  - Remetente/Destinatário
  - Banco
  - Tipo da transação
- 📊 Registro automático em uma planilha Google Sheets
- ✅ Testes automatizados com Pytest

---

# 🔄 Fluxo da aplicação

```text
Notificação Android
        │
        ▼
      Tasker
        │
HTTP POST (JSON)
        │
        ▼
 Django View
        │
        ▼
TransactionService
        │
        ▼
Parser específico do banco
        │
        ▼
Dataclass Transacao
        │
        ▼
GoogleSheetsService
        │
        ▼
Google Sheets
```

---

# 📂 Estrutura do projeto

```
app/
│
├── core/          # Objetos de domínio, enums e regras centrais
├── parsers/       # Parsers específicos de cada banco
├── services/      # Serviços da aplicação
├── tests/         # Testes automatizados
├── utils/         # Funções utilitárias
│
├── views.py
├── models.py
└── config.py
```

---

# 🛠 Tecnologias

- Python
- Django
- Google Sheets API
- gspread
- Regex
- Pytest
- Tasker (Android)

---

# 🧪 Testes

```bash
pytest
```

---

# 🚀 Próximos passos

- [ ] Suporte a novos bancos
- [ ] Categorização automática de gastos
- [ ] Dashboard financeiro
- [ ] Relatórios mensais
- [ ] Deploy em produção (Render)

---

## 📖 Motivação

Este projeto nasceu para eliminar o lançamento manual de despesas em planilhas.

Sempre que uma nova transação é realizada, basta a notificação chegar ao celular para que todo o processo de interpretação e registro aconteça automaticamente.

Além da utilidade prática no dia a dia, o projeto também foi desenvolvido como forma de aprofundar conhecimentos em arquitetura de software, integração de APIs, testes automatizados e processamento de texto com Regex.
