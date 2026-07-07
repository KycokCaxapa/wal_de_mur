from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from src.core.config import settings


class IsAdmin(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool:
        user = event.from_user
        return user is not None and user.id == settings.ADMIN
