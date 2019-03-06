import Voss_RoboPiLib as RPL
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

speed.1 = 500
speed.2 = 2000
speed.3 = 0

def extend():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed.1, speed.1 * 2)
  
def retract():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed.2, speed.2 * 2)

def stop():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed.3, speed.3 * 2)
