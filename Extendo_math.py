import Voss_RoboPiLib as RPL
import fractions
from time import sleep
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)
rate = 2.1
def movement():
  tm = fractions.Fraction(distance, rate)
  if distance > 0:
    speed = 500
  else:
    speed = 2000
  print(tm)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed, speed * 2)
  sleep(abs(tm))
  RPL.pwmWrite(0, 0, 1)
while True:
  distance = input('- ')
  movement()
  continue
