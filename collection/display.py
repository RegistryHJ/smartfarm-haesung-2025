import uasyncio as asyncio
from utime import sleep

class Display:
  # 생성자
  def __init__(self, rtc, aht, ens, light, oled, team):
    self.rtc = rtc
    self.aht = aht
    self.ens = ens
    self.light = light
    self.oled = oled
    self.team = team
    self.active = False

  # start 비동기 함수
  async def start(self):
    """OLED에 화면 표출을 시작하는 함수"""
    self.active = True
    while self.active:
      now = self.rtc.get_rtc_time()
      temp = self.aht.read()[1]
      co2 = self.ens.CO2
      light = self.light.measurement

      self.oled.fill(0)
      self.oled.text(f"[{self.team}]", 0, 0)
      self.oled.text(f"Date: {now[0]}-{now[1]}-{now[2]}", 0, 10)
      self.oled.text(f"Time: {now[4]}:{now[5]}:{now[6]}", 0, 20)
      self.oled.text(f"Temp: {temp:.2f} Deg", 0, 30)
      self.oled.text(f"CO2: {co2} ppm", 0, 40)
      self.oled.text(f"Light: {light:.0f} lx", 0, 50)
      self.oled.show()
      await asyncio.sleep(0.5)

  # stop 함수
  def stop(self):
    """OLED에 화면 표출을 정지하는 함수"""
    self.active = False
    self.oled.fill(0)
    self.oled.show()
    sleep(0.5)
