from datetime import datetime

from src.server.devices.models import Device


devices: list[Device] = []


def add_device(ip: str, user_agent: str) -> Device:
    device = Device(
        id=len(devices) + 1,
        ip=ip,
        user_agent=user_agent,
        name=detect_name(user_agent),
        connected_at=datetime.now()
    )
    devices.append(device)

    return device


def detect_name(user_agent: str) -> str:
    ua = user_agent.lower()

    if 'iphone' in ua:
        return '📱 iPhone'

    if 'android' in ua:
        return '📱 Android'

    if 'macintosh' in ua:
        return '💻 Mac'

    if 'windows' in ua:
        return '🖥 Windows'

    return '❓ Unknown'



def get_devices() -> list[Device]:
    return devices
