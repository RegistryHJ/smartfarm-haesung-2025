from machine import Pin, I2C
from utime import sleep
from aht21 import AHT21

aht = AHT21(I2C(1, sda=Pin(14), scl=Pin(15), freq=400000))

while True:
  print(aht.read()[1])
  sleep(1)
