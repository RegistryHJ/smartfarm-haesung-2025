from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))

oled.line(32, 32, 96, 32, 1)  # (32, 32)에서 (96, 32)까지 수평선 그리기
oled.show()
