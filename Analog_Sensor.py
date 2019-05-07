import RoboPiLib as RPL
import setup

sensor_pin = 14
sense = RPL.analogRead(sensor_pin)
print sense
