import machine
import urequests


def update(server: str) -> bool:
    response = urequests.get(f'{server}/ota/update')
    code = response.text

    if response.status_code == 204:
        response.close()
        return False

    response.close()

    with open('main.py', 'w') as file:
        print('[READ]')
        file.write(code)

    machine.reset()
    return True
