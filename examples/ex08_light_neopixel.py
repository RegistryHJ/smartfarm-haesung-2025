from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750
from neopixel import NeoPixel

light = BH1750(0x23, I2C(0, sda=Pin(4), scl=Pin(5)))
np = NeoPixel(Pin(21), 1)

while True:
  print(light.measurement)        # 조도센서 측정값 출력
  if light.measurement >= 750:    # 조도센서 측정값이 750lx 이상이면
    np[0] = (255, 0, 0)           # NeoPixel 빨강색 점등
  elif light.measurement >= 500:  # 조도센서 측정값이 500lx 이상이면
    np[0] = (0, 255, 0)           # NeoPixel 초록색 점등
  elif light.measurement >= 250:  # 조도센서 측정값이 250lx 이상이면
    np[0] = (0, 0, 255)           # NeoPixel 파랑색 점등
  else:                           # 아니면 (250lx 미만이면)
    np[0] = (0, 0, 0)             # NeoPixel 끄기
  np.write()                      # NeoPixel 출력
  sleep(1)
