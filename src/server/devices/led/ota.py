from fastapi.responses import FileResponse, Response
from fastapi import APIRouter

from src.server.devices.services import led


router = APIRouter(prefix='/ota')


@router.get('/update')
async def ota_update():
    return FileResponse(
        'src/server/devices/led/firmware/main.py',
        media_type='text/plain'
    )


@router.post('/publish')
async def ota_publish():
    led.update = True

    return {'ok': True}
