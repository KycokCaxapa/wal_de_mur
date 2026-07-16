from datetime import datetime

from src.server.devices.models import LED, Device


devices: list[Device] = []
led = LED(
    id=0,
    ip='localhost',
    name='Built-in LED',
    connected_at=datetime.now(),
    state=False,
    update=False
)


def register_device(data: Device) -> tuple[Device, bool]:
    for device in devices:
        if device.ip == data.ip:
            device.name = data.name
            device.connected_at = datetime.now()
            return device, False

    device = Device(
        id=len(devices) + 1,
        ip=data.ip,
        name=data.name,
        connected_at=datetime.now()
    )

    devices.append(device)

    return device, True
