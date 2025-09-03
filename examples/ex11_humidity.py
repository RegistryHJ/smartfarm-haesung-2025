from machine import Pin, I2C
from utime import sleep
from aht21 import AHT21

aht = AHT21(I2C(1, sda=Pin(2), scl=Pin(3), freq=400000))

while True:
  print(aht.read()[0])
  sleep(1)
