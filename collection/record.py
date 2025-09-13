import os
import uasyncio as asyncio
from utime import sleep

class Record:
  # 생성자
  def __init__(self, rtc, aht, ens, light, interval):
    self.rtc = rtc
    self.aht = aht
    self.ens = ens
    self.light = light
    self.interval = interval
    self.file = None
    self.active = False

  # start 비동기 함수
  async def start(self):
    """데이터 기록을 시작하는 함수"""
    self.active = True
    self.file = open("data.csv", "a")
    print("Recording started!")
    print("Recording...")

    try:
      while self.active:
        now = self.rtc.get_rtc_time()
        temp = self.aht.read()[1]
        co2 = self.ens.CO2
        light = self.light.measurement

        self.file.write(f"{now[0]}-{now[1]}-{now[2]}, {now[4]}:{now[5]}:{now[6]}, {temp:.2f}, {co2}, {light:.0f}\n")
        self.file.flush()
        await asyncio.sleep(self.interval)
    except Exception as e:
      print(e)

  # stop 함수
  def stop(self):
    """데이터 기록을 정지하는 함수"""
    self.active = False
    self.file.close() if self.file else None
    print("Recording stopped!")
    print("File Saved!")
