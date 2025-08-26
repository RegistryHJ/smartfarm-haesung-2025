from machine import Pin
from utime import sleep
from neopixel import NeoPixel

np = NeoPixel(machine.Pin(21), 1)

# NeoPixel On 함수
def neopixel_on():
  for i in range(0, np.n):
    np[i] = (25, 25, 25)
  np.write()

# NeoPixel Off 함수
def neopixel_off():
  for i in range(0, np.n):
    np[i] = (0, 0, 0)
  np.write()

while True:
  neopixel_on()   # NeoPixel를 켭니다.
  sleep(0.5)      # 0.5초 대기
  neopixel_off()  # NeoPixel를 끕니다.
  sleep(0.5)      # 0.5초 대기
