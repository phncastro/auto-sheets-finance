import gspread
from google.oauth2.service_account import Credentials
from app.config import GOOGLE_SHEETS_NAME, GOOGLE_CREDENTIALS

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS,
    scopes=scopes
)

client = gspread.authorize(creds)

planilha = client.open(GOOGLE_SHEETS_NAME)

aba = planilha.sheet1

class GoogleSheetsService:

    def adicionar_transacao(self, transacao):
        ...