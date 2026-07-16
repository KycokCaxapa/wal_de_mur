from machine import Pin
import network
import time
import urequests

import ota

from config import WIFI, WIFI_PASSWORD, SERVER_URL


led = Pin(2, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI, WIFI_PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

print('Wi-Fi:', wlan.ifconfig())

while True:
    try:
        response = urequests.get(f'{SERVER_URL}/devices/led')
        command = response.json()
        response.close()

        print('Polling..')

        if command.get('LED') is not None:
            led.value(command['LED'])

        if command.get('OTA'):
            print('Starting OTA update...')
            ota.update(SERVER_URL)

    except Exception as e:
        print('ERROR:', e)

    time.sleep(0.5)
