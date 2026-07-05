from fastapi import APIRouter, Request

from src.telegram_bot.handlers.devices import notify_device
from src.server.devices.manager import add_device
from src.core.bot import bot

router = APIRouter()


@router.get('/')
async def index(request: Request):
    ip = request.client.host
    user_agent = (
        request.headers.get(
            'user-agent',
            'unknown'
        )
    )
    device = add_device(
        ip=ip,
        user_agent=user_agent
    )

    await notify_device(device, bot)

    return {
        'status': 'connected',
        'device': device.name
    }
