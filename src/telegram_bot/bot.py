from aiogram import Bot, Dispatcher

from telegram_bot.config import settings
from src.telegram_bot.handlers import start


bot = Bot(token=settings.TOKEN)
dp = Dispatcher()


def register_handlers():
    dp.include_router(start.router)


async def start_bot():
    register_handlers()

    await dp.start_polling(bot)
