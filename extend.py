import Voss_RoboPiLib as RPL
# RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)
RPL.init()

speed = 500

def extend():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed, speed * 2)

extend()
