from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from src.telegram_bot.handlers.admin_filter import IsAdmin
from src.server.devices.services import devices
from src.server.devices.models import Device
from src.core.config import settings


router = Router()
router.message.filter(IsAdmin())
router.callback_query.filter(IsAdmin())


async def notify_device(device: Device, bot) -> None:
    text = (
        '🚨 Новое подключение\n\n'

        f'Устройство: {device.name}\n'
        f'ID: {device.id}\n'

        f'🌐 IP: {device.ip}\n'

        f'Подключено в {device.connected_at}'
    )

    await bot.send_message(chat_id=settings.ADMIN, text=text)


@router.message(Command('devices'))
async def devices_command(message: Message):
    if not devices:
        await message.answer(
            'Нет подключенных устройств'
        )
        return

    text = '📡 Устройства:\n\n'

    for device in devices:
        text += (
            f'{device.name}\n'
            f'ID: {device.id}\n'
            f'IP: {device.ip}\n'
            f'Устройство: {device.name}\n'
            f'Подключено в: {device.connected_at}\n\n'
        )

    await message.answer(text)
