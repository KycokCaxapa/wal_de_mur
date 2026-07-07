from machine import Pin
import urequests
import network
import time

from config import WIFI, WIFI_PASSWORD, SERVER_URL

URL = f'{SERVER_URL}/devices/led'

led = Pin(2, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI, WIFI_PASSWORD)

while not wlan.isconnected():
    time.sleep(0.5)

while True:
    try:
        response = urequests.get(URL)
        command = response.json()
        response.close()

        if command['LED'] is not None:
            led.value(command['LED'])
        
        print('Polling server...')

    except Exception as e:
        print(e)

    time.sleep(0.2)
