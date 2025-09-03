from machine import Pin, I2C
from utime import sleep
from ens160 import ENS160
from neopixel import NeoPixel

gas = ENS160(I2C(1, sda=Pin(2), scl=Pin(3), freq=400000))
np = NeoPixel(Pin(21), 1)

gas.reset()                   # 가스센서 리셋
sleep(0.5)
gas.operating_mode = 2        # 측정모드 설정
sleep(2)

while True:
  print(gas.AQI)
  if gas.AQI == 1:
    np[0] = (0, 0, 255)       # NeoPixel 파란색 점등
  elif gas.AQI == 2:
    np[0] = (0, 255, 255)     # NeoPixel 하늘색 점등
  elif gas.AQI == 3:
    np[0] = (0, 255, 0)       # NeoPixel 초록색 점등
  elif gas.AQI == 4:
    np[0] = (255, 255, 0)     # NeoPixel 노란색 점등
  elif gas.AQI == 5:
    np[0] = (255, 0, 0)       # NeoPixel 빨간색 점등
  np.write()
  sleep(1)
