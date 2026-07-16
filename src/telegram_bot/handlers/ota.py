import aiohttp

from aiogram.types import CallbackQuery
from aiogram import F, Router

from src.telegram_bot.handlers.admin_filter import IsAdmin
from src.telegram_bot.keyboards import main_ikb
from src.server.devices.services import led
from src.core.config import settings


url = settings.SERVER_URL
router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


@router.callback_query(F.data == 'ota_update')
async def led_on(callback: CallbackQuery) -> None:
    async with aiohttp.ClientSession() as session:
        await session.post(f'{url}/ota/publish')
    
    
    await callback.answer('🔄 Обновление...')
