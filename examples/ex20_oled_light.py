from machine import Pin, SoftI2C
from utime import sleep
from ssd1306 import SSD1306_I2C
from bh1750 import BH1750

oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))
light = BH1750(0x23, SoftI2C(sda=Pin(4), scl=Pin(5)))

while True:
  oled.fill(0)                                     # 화면 지우기
  oled.text(f"{light.measurement:.2f} lx", 0, 32)  # 조도센서 측정값 출력
  oled.show()                                      # 화면 표시하기
  sleep(1)
