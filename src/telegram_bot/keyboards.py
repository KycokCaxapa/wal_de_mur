from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.server.devices.manager import led


def led_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text='☀️ Свет: включен' if led.state else '🌑 Свет: выключен',
        callback_data='toggle_led'
    )

    return builder.as_markup()
