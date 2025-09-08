from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))

oled.pixel(64, 32, 1)  # 화면 가운데에 점 찍기
oled.show()
