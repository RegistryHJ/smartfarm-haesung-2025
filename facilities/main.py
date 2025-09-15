from machine import Pin, PWM
from utime import sleep
from neopixel import NeoPixel
from boot import Boot

# 직접 입력하여 설정하세요!
np0_color = (0, 50, 0)       # DataPi NeoPixel 색상을 지정하세요! (Default: Green)
np1_color = (255, 255, 255)  # NeoPixel 1번 스트립 색상을 지정하세요! (Default: White)
np2_color = (255, 255, 255)  # NeoPixel 2번 스트립 색상을 지정하세요! (Default: White)

# 전역 변수
active = False
np_off = (0, 0, 0)

# HW 인스턴스 생성
btn = Pin(20, Pin.IN, Pin.PULL_UP)
bz = PWM(Pin(22))
fan = Pin(10, Pin.OUT)
np0 = NeoPixel(Pin(21), 1)
np1 = NeoPixel(Pin(6), 30)
np2 = NeoPixel(Pin(7), 30)
boot = Boot(np0, bz)

# 모듈 인스턴스 생성
boot = Boot(np0, bz)

# status_np0 함수
def status_np0():
  """NeoPixel로 시스템 상태를 알리는 함수"""
  if active:
    np0[0] = np0_color
    np0.write()
  else:
    np0[0] = np_off
    np0.write()

# status_bz 함수
def status_bz():
  """Buzzer로 시스템 상태를 알리는 함수"""
  freqs = [1000, 2000]

  if active:
    for freq in freqs:
      bz.freq(freq)
      bz.duty_u16(30000)
      sleep(0.1)
  else:
    for freq in reversed(freqs):
      bz.freq(freq)
      bz.duty_u16(30000)
      sleep(0.1)

  bz.duty_u16(0)

# ctl_strip_np1 함수
def ctl_strip_np1():
  """NeoPixel 1번 스트립 제어 함수"""
  if active:
    for i in range(0, np1.n):
      np1[i] = np1_color
    np1.write()
  else:
    for i in range(0, np1.n):
      np1[i] = np_off
    np1.write()

# ctl_strip_np2 함수
def ctl_strip_np2():
  """NeoPixel 2번 스트립 제어 함수"""
  if active:
    for i in range(0, np2.n):
      np2[i] = np2_color
    np2.write()
  else:
    for i in range(0, np2.n):
      np2[i] = np_off
    np2.write()

# ctl_fan 함수
def ctl_fan():
  """Fan 제어 함수"""
  fan.value(active)

# btn_handler 함수
def btn_handler(pin):
  """버튼 핸들러 함수"""
  global active
  active = not active
  status_np0()
  status_bz()
  ctl_strip_np1()
  ctl_strip_np2()
  ctl_fan()

# btn_handler 함수를 Button IRQ에 바인딩
btn.irq(trigger=Pin.IRQ_FALLING, handler=btn_handler)

# main 함수
def main():
  boot.boot()
  while True:
    sleep(1)

# main 함수 실행
if __name__ == "__main__":
  main()
