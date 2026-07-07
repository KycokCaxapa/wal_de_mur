import aiohttp

from aiogram.types import CallbackQuery
from aiogram import F, Router

from src.telegram_bot.handlers.admin_filter import IsAdmin
from src.telegram_bot.keyboards import led_keyboard
from src.server.devices.manager import led
from src.core.config import settings


url = settings.SERVER_URL
router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.callback_query(F.data == 'toggle_led')
async def led_on(callback: CallbackQuery) -> None:
    async with aiohttp.ClientSession() as session:
        await session.post(f'{url}/devices/led/switch')
    
    await callback.answer('☀️ Свет включён' if led.state else '🌑 Свет выключен')
    await callback.message.edit_reply_markup(reply_markup=led_keyboard())
