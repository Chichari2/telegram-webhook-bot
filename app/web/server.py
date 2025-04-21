from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from injector import inject, Injector
from app.core.di import injector
from app.handlers.commands import CommandHandlers
from app.handlers.callbacks import CallbackHandlers
from app.core.config import settings


async def on_startup(app):
  """Initialize bot and dispatcher on application startup."""
  bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
  storage = MemoryStorage()
  dp = Dispatcher(bot, storage=storage)

  # Initialize handlers with DI
  command_handlers = injector.get(CommandHandlers)
  callback_handlers = injector.get(CallbackHandlers)

  # Set webhook
  await bot.set_webhook(settings.TELEGRAM_WEBHOOK_URL)

  app["bot"] = bot
  app["dp"] = dp


async def on_shutdown(app):
  """Cleanup on application shutdown."""
  bot: Bot = app["bot"]
  await bot.delete_webhook()
  await bot.close()


async def handle_webhook(request):
  """Handle incoming Telegram updates."""
  bot: Bot = request.app["bot"]
  dp: Dispatcher = request.app["dp"]

  update = types.Update(**await request.json())
  await dp.process_update(update)

  return web.Response()


def create_app():
  """Create aiohttp application."""
  app = web.Application()
  app.on_startup.append(on_startup)
  app.on_shutdown.append(on_shutdown)
  app.add_routes([web.post("/webhook", handle_webhook)])
  return app