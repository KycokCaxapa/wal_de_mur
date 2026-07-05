from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from src.core.config import settings


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    user = message.from_user
    admin_text = (
        '🚨 Новый вход в бота\n\n'

        f'👤 Имя: {user.full_name}\n'
        f'🆔 ID: {user.id}\n'
        f'📱 Username: {f'@{user.username}' if user.username else ''}\n'
        f'🌍 Язык: {user.language_code}\n'
        f'🤖 Бот: {'Бот' if user.is_bot else 'Не бот'}\n'
        f'⭐ Премиум: {'Да' if getattr(user, 'is_premium', False) else 'Нет'}'
    )

    await message.bot.send_message(
        chat_id=settings.ADMIN,
        text=admin_text
    )

    await message.answer(
        'Привет! 👋\n'
        'Ты успешно подключился.'
    )
