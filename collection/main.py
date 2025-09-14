import uasyncio as asyncio
from machine import Pin, I2C, SoftI2C, PWM
from utime import sleep
from wlan import WLAN
from soft_rtc import SoftRTC
from neopixel import NeoPixel
from aht21 import AHT21
from ens160 import ENS160
from bh1750 import BH1750
from ssd1306 import SSD1306_I2C
from boot import Boot
from display import Display
from record import Record

# 직접 입력하여 설정하세요!
team_name = "*"            # 팀 이름을 영문으로 입력하세요!
ssid, password = "*", "*"  # WiFi SSID와 Password를 입력하세요!

# 전역 변수
active = False
interval = 600

# HW 인스턴스 생성
btn = Pin(20, Pin.IN, Pin.PULL_UP)
np = NeoPixel(Pin(21), 1)
bz = PWM(Pin(22))
wlan_0 = WLAN(ssid, password)
rtc = SoftRTC()
aht = AHT21(I2C(1, sda=Pin(2), scl=Pin(3), freq=400000))
ens = ENS160(I2C(1, sda=Pin(2), scl=Pin(3), freq=400000))
light = BH1750(0x23, SoftI2C(sda=Pin(4), scl=Pin(5)))
oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))

# ENS 센서 리셋 및 측정모드 설정
ens.reset()
sleep(2)
ens.operating_mode = 2
sleep(2)

# 모듈 인스턴스 생성
boot = Boot(np, bz, oled)
display = Display(rtc, aht, ens, light, oled, team_name)
record = Record(rtc, aht, ens, light, interval)

# status_np 비동기 함수
async def status_np():
  """NeoPixel로 시스템 상태를 알리는 함수"""
  is_incresed = True
  brightness = 0

  while True:
    if active:
      if is_incresed:
        brightness += 1
        if brightness >= 50:
          is_incresed = False
      else:
        brightness -= 1
        if brightness <= 0:
          is_incresed = True
    else:
      brightness = 0

    np[0] = (0, brightness, 0)
    np.write()

    await asyncio.sleep(0.025)

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

# status_oled 함수
def status_oled():
  """OLED로 시스템 상태를 표출하는 함수"""
  oled.fill(0)
  if active:
    oled.text("Record Started!", 0, 0)
  else:
    oled.text("Record Stopped!", 0, 0)
  oled.show()

# start_system 비동기 함수
async def start_system():
  """시스템을 시작하는 비동기 함수"""
  while True:
    if active:
      await asyncio.gather(display.start(), record.start())
    await asyncio.sleep(0.1)

# btn_handler 함수
def btn_handler(pin):
  """버튼 핸들러 함수"""
  global active
  active = not active
  if not active:
    display.stop()
    record.stop()
  status_oled()
  status_bz()

# btn_handler 함수를 Button IRQ에 바인딩
btn.irq(trigger=Pin.IRQ_FALLING, handler=btn_handler)

# main 함수
async def main():
  wlan_0.connect(oled)
  rtc.set_rtc_time()
  now = rtc.get_rtc_time()
  print(f"RTC Time: {now[0]}-{now[1]}-{now[2]} {now[4]}:{now[5]}:{now[6]}")
  boot.boot()
  await asyncio.gather(status_np(), start_system())

# main 함수 비동기 실행
asyncio.run(main())
