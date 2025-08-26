from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

while True:
  led.on()      # LED를 켭니다.
  sleep(0.5)    # 0.5초 대기
  led.off()     # LED를 끕니다.
  sleep(0.5)    # 0.5초 대기
  # led.toggle()  # LED 상태를 반전시킵니다.
