from machine import Pin, I2C
from utime import sleep
from ens160 import ENS160

gas = ENS160(I2C(1, sda=Pin(14), scl=Pin(15), freq=400000))

gas.reset()                   # 가스센서 리셋
sleep(0.5)
gas.operating_mode = 2        # 측정모드 설정
sleep(2)

while True:
  print("----------------")
  print(f"AQI: {gas.AQI}")    # 공기질 지수
  print(f"CO2: {gas.CO2}")    # 이산화탄소 농도
  print(f"TVOC: {gas.TVOC}")  # 휘발성 유기화합물 농도
  sleep(1)
