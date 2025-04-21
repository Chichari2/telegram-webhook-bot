from aiogram import types
from aiogram.dispatcher import Dispatcher
from injector import inject
from app.services.api_client import JsonPlaceholderClient
from app.services.data_processor import DataProcessor
from app.db.repository import PostRepository
from app.services.google_sheets import GoogleSheetsService


class CallbackHandlers:
  """Handlers for Telegram bot callbacks."""

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
    """Register all callback handlers."""
    self.dp.register_callback_query_handler(
      self.handle_get_posts, lambda c: c.data == "get_posts"
    )
    self.dp.register_callback_query_handler(
      self.handle_get_post, lambda c: c.data.startswith("get_post_")
    )

  async def handle_get_posts(self, callback_query: types.CallbackQuery):
    """Handle 'get_posts' callback."""
    await callback_query.answer()

    try:
      # Get data from API
      raw_posts = await self.api_client.get_posts()

      # Process data
      processed_posts = await self.data_processor.process_posts(raw_posts)

      # Save to database
      for post in processed_posts:
        await self.post_repo.create_post(post)

      # Save to Google Sheets
      await self.google_sheets.append_data(
        "Posts",
        [post.dict() for post in processed_posts]
      )

      await callback_query.message.answer(
        f"Successfully fetched and saved {len(processed_posts)} posts!"
      )
    except Exception as e:
      await callback_query.message.answer(
        f"Error occurred: {str(e)}"
      )

  async def handle_get_post(self, callback_query: types.CallbackQuery):
    """Handle 'get_post_*' callback."""
    await callback_query.answer()
    post_id = int(callback_query.data.split("_")[-1])

    try:
      # Get data from API
      raw_post = await self.api_client.get_post(post_id)

      # Process data
      processed_post = (await self.data_processor.process_posts([raw_post]))[0]

      # Save to database
      await self.post_repo.create_post(processed_post)

      # Save to Google Sheets
      await self.google_sheets.append_data(
        "Posts",
        [processed_post.dict()]
      )

      await callback_query.message.answer(
        f"Successfully fetched and saved post #{post_id}!"
      )
    except Exception as e:
      await callback_query.message.answer(
        f"Error occurred: {str(e)}"
      )