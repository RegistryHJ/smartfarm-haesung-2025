from machine import Pin
from utime import sleep
from neopixel import NeoPixel

np = NeoPixel(machine.Pin(21), 1)

np[0] = (25, 25, 25)  # NeoPixel의 색상과 밝기 설정
np.write()            # NeoPixel에 색상 적용
