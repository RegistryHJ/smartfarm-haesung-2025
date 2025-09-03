from machine import Pin, I2C, PWM
from utime import sleep
from aht21 import AHT21

aht = AHT21(I2C(1, sda=Pin(2), scl=Pin(3), freq=400000))
bz = PWM(Pin(22))

while True:
  print(aht.read()[1])
  if aht.read()[1] >= 36.5:   # 온도가 36.5도 이상이면
    bz.freq(500)              # Buzzer 주파수를 500Hz로 설정
    bz.duty_u16(1000)         # Buzzer 켜기
  else:                       # 아니면 (36.5도 미만이면)
    bz.duty_u16(0)            # Buzzer 끄기
  sleep(0.5)
