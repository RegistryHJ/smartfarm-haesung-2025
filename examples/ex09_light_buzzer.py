from machine import Pin, I2C, PWM
from utime import sleep
from bh1750 import BH1750

light = BH1750(0x23, I2C(0, sda=Pin(4), scl=Pin(5)))
bz = PWM(Pin(22))

while True:
  print(light.measurement)      # 조도센서 측정값 출력
  if light.measurement >= 500:  # 조도센서 측정값이 500lx 이상이면
    bz.freq(500)                # Buzzer 주파수를 500Hz로 설정
    bz.duty_u16(1000)           # Buzzer 켜기
  else:                         # 아니면 (500lx 미만이면)
    bz.duty_u16(0)              # Buzzer 끄기
  sleep(1)
