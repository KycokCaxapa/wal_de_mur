from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from src.server.devices.services import led


def main_ikb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text='☀️ Свет: включен' if led.state else '🌑 Свет: выключен',
        callback_data='toggle_led'
    )
    builder.button(
        text='🔄 Обновить плату',
        callback_data='ota_update'
    )

    builder.adjust(1)

    return builder.as_markup()
