import Voss_RoboPiLib as RPL
from time import sleep
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)
rate = 2
speed = 500
def movement():
  tm = rate / distance
  if distance > 0:
    RPL.pinMode(0, RPL.PWM)
  else distance < 0:
    RPL.pinMode(1, RPL.PWM)
  RPL.pwmWrite(0, speed, speed * 2)
  sleep(tm)
while True:
  distance = input('- ')
  movement()
  continue
