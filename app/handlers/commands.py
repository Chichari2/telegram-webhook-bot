from aiogram import types
from aiogram.dispatcher import Dispatcher
from injector import inject
from app.services.api_client import JsonPlaceholderClient
from app.services.data_processor import DataProcessor
from app.db.repository import PostRepository
from app.services.google_sheets import GoogleSheetsService


class CommandHandlers:
  """Handlers for Telegram bot commands."""

  @inject
  def __init__(
    self,
    dp: Dispatcher,
    api_client: JsonPlaceholderClient,
    data_processor: DataProcessor,
    post_repo: PostRepository,
    google_sheets: GoogleSheetsService
  ):
    self.dp = dp
    self.api_client = api_client
    self.data_processor = data_processor
    self.post_repo = post_repo
    self.google_sheets = google_sheets
    self.register_handlers()

  def register_handlers(self):
    """Register all command handlers."""
    self.dp.register_message_handler(self.start, commands=["start"])

  async def start(self, message: types.Message):
    """Handle /start command with inline buttons."""
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
      types.InlineKeyboardButton(text="Get Posts", callback_data="get_posts"),
      types.InlineKeyboardButton(text="Get Post #1", callback_data="get_post_1")
    ]
    keyboard.add(*buttons)

    await message.answer(
      "Welcome to JSON Placeholder Bot!\n"
      "Choose an action:",
      reply_markup=keyboard
    )