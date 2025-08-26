from machine import Pin, PWM
from utime import sleep

bz = PWM(Pin(22))

bz.freq(500)        # Buzzer 주파수를 500Hz로 설정
bz.duty_u16(1000)   # Buzzer Duty Cycle을 1000으로 설정 (0~65535)
sleep(1)            # 1초 대기
bz.deinit()         # Buzzer를 끕니다.
