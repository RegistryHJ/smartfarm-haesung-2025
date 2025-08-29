from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750

light = BH1750(0x23, I2C(0, sda=Pin(4), scl=Pin(5)))

while True:
  print(light.measurement)  # 조도센서 측정값 출력
  sleep(1)
