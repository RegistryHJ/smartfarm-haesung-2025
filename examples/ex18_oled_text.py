from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

oled = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))

oled.text("Hello!", 0, 32)  # (0, 32) 위치에 텍스트 출력
oled.show()
