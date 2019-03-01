import Voss_RoboPiLib as RPL
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)


def calibrate():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, 2000 * 2, 3000)

calibrate()
