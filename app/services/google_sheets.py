import gspread
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Dict
from app.core.config import settings


class GoogleSheetsService:
  """Service for interacting with Google Sheets."""

  def __init__(self):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
      settings.GOOGLE_SHEETS_CREDENTIALS, scope)
    self.client = gspread.authorize(creds)

  async def append_data(self, sheet_name: str, data: List[Dict]) -> None:
    """Append data to a Google Sheet."""
    sheet = self.client.open_by_key(settings.GOOGLE_SHEET_ID).worksheet(sheet_name)
    values = [[item[key] for key in item.keys()] for item in data]
    sheet.append_rows(values)