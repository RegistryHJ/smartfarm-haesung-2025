from machine import Pin, SoftI2C
from utime import sleep
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))

pos_x = 0                             # 텍스트의 X좌표 초기값
pos_y = 32                            # 텍스트의 Y좌표 초기값

while True:
  oled.fill(0)                        # 화면 지우기
  oled.text("Hello!", pos_x, pos_y)   # (pos_x, pos_y) 위치에 텍스트 출력
  oled.show()                         # 화면 표시하기
  pos_x += 1                          # X좌표 1씩 증가
  sleep(0.5)
