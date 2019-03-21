import Voss_RoboPiLib as RPL
from time import sleep
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)
rate = 2
def movement():
  tm = abs(rate / distance)
  if distance > 0:
    speed = 500
  else:
    speed = 2000
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed, speed * 2)
  sleep(tm)
  RPL.pwmWrite(0, 0, 1)
while True:
  distance = input('- ')
  movement()
  continue
