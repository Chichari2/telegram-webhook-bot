from injector import Injector, singleton, Module
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session
from app.db.repository import PostRepository
from app.services.api_client import JsonPlaceholderClient
from app.services.google_sheets import GoogleSheetsService
from app.services.data_processor import DataProcessor


class AppModule(Module):
  def configure(self, binder):
    # Database
    binder.bind(AsyncSession, to=async_session, scope=singleton)
    binder.bind(PostRepository, scope=singleton)

    # Services
    binder.bind(JsonPlaceholderClient, scope=singleton)
    binder.bind(GoogleSheetsService, scope=singleton)
    binder.bind(DataProcessor, scope=singleton)


injector = Injector([AppModule()])