import Voss_RoboPiLib as RPL
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

speed = 1000

def calibrate():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed * 2, speed)   #RPL.pwmWrite(0, 1000 * 2, 3000)

calibrate()
