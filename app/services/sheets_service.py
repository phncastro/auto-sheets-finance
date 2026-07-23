import gspread
from google.oauth2.service_account import Credentials
from app.core.transaction import Transacao
import os
from dotenv import load_dotenv

class GoogleSheetsService:

    def __init__(self):

        load_dotenv()

        sheets_name = os.getenv("GOOGLE_SHEETS_NAME")
        google_credentials = os.getenv("GOOGLE_CREDENTIALS")
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            google_credentials,
            scopes=scopes
        )

        self.client = gspread.authorize(creds)
        self.planilha = self.client.open(sheets_name)
        self.aba = self.planilha.sheet1


    def adicionar(self, transacao: Transacao):

        self.aba.append_row(transacao.linha())