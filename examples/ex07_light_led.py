from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750

light = BH1750(0x23, I2C(0, sda=Pin(4), scl=Pin(5)))
led = Pin('LED', Pin.OUT)

while True:
  print(light.measurement)      # 조도센서 측정값 출력
  if light.measurement >= 500:  # 조도센서 측정값이 500lx 이상이면
    led.off()                   # LED 끄기
  else:                         # 아니면 (500lx 미만이면)
    led.on()                    # LED 켜기
  sleep(1)
