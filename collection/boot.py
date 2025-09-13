from utime import sleep

class Boot:
  # 생성자
  def __init__(self, np, bz, oled):
    self.colors = [(50, 0, 0), (0, 50, 0), (0, 0, 50), (0, 0, 0)]
    self.freqs = [1000, 2000, 3000]
    self.np = np
    self.bz = bz
    self.oled = oled

  # start_message 함수
  def start_message(self):
    """부팅 시작 메시지 출력 함수"""
    print("Booting...")
    self.oled.fill(0)
    self.oled.text("Booting...", 0, 0)
    self.oled.show()

  # complete_message 함수
  def complete_message(self):
    """부팅 완료 메시지 출력 함수"""
    print("Boot Complete!")
    self.oled.fill(0)
    self.oled.text("Boot Complete!", 0, 0)
    self.oled.show()

  # boot_np 함수
  def boot_np(self):
    """NeoPixel 부팅 애니메이션 함수"""
    for color in self.colors:
      self.np[0] = color
      self.np.write()
      sleep(0.25)

  # boot_bz 함수
  def boot_bz(self):
    """Buzzer 부팅음 재생 함수"""
    for freq in self.freqs:
      self.bz.freq(freq)
      self.bz.duty_u16(30000)
      sleep(0.1)
    self.bz.duty_u16(0)

  # boot 함수
  def boot(self):
    self.start_message()
    self.boot_np()
    self.boot_bz()
    self.complete_message()
