from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from src.server.devices.manager import get_devices
from src.server.devices.models import Device
from src.core.config import settings


router = Router()


async def notify_device(device: Device, bot) -> None:
    text = (
        '🚨 Новое устройство\n\n'

        f'Название: {device.name}\n'
        f'ID: {device.id}\n'

        f'🌐 IP:\n'
        f'{device.ip}\n'

        f'🧩 User-Agent:\n'
        f'{device.user_agent}\n\n'

        f'⏰ Подключено:\n'
        f'{device.connected_at}'
    )

    await bot.send_message(chat_id=settings.ADMIN, text=text)


@router.message(Command('devices'))
async def devices_command(message: Message):
    devices = get_devices()

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
            f'UA: {device.user_agent}\n'
            f'Подключен: {device.connected_at}\n\n'
        )


    await message.answer(
        text
    )