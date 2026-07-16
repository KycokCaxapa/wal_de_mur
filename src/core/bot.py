from aiogram import Bot, Dispatcher

from src.telegram_bot.handlers.devices import router as devices_router
from src.telegram_bot.handlers.start import router as start_router
from src.telegram_bot.handlers.led import router as led_router
from src.telegram_bot.handlers.ota import router as ota_router
from src.core.config import settings


bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

dp.include_routers(start_router,
                   devices_router,
                   led_router,
                   ota_router)
