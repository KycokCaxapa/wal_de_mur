from fastapi import APIRouter, Request
from datetime import datetime

from src.telegram_bot.handlers.devices import notify_device
from src.server.devices.manager import devices, led, register_device
from src.server.devices.models import Device
from src.core.bot import bot

router = APIRouter()


@router.get('/')
async def index():
    return {'status': 'ok'}


@router.post('/devices/register')
async def register_device_endpoint(request: Request) -> dict[str, bool]:
    device, is_new = register_device(
        Device(
            id=len(devices),
            ip=request.client.host,
            name=request.headers.get('user-agent', 'unknown'),
            connected_at=datetime.now()
        )
    )

    if is_new:
        await notify_device(device, bot)

    return {'ok': True}


@router.post('/devices/led/switch')
async def led_switch():
    led.state = not led.state
    print(f'[{led.state}]')
    
    return {'ok': True}


@router.get('/devices/led')
async def get_led_state():
    state = led.state

    return {
        'LED': state
    }
