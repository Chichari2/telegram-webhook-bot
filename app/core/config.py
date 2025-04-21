from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
  TELEGRAM_BOT_TOKEN: str
  TELEGRAM_WEBHOOK_URL: str
  POSTGRES_DSN: PostgresDsn
  GOOGLE_SHEETS_CREDENTIALS: str
  GOOGLE_SHEET_ID: str
  API_BASE_URL: str = "https://jsonplaceholder.typicode.com"

  class Config:
    env_file = ".env"


settings = Settings()