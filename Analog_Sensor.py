import RoboPiLib as RPL
import setup

sensor_pin = 1
sense = RPL.analogRead(sensor_pin)
print sense

#RoboPi.pinMode(17,RoboPi.PWM)
#RoboPi.analogWrite(17,127) 
#print RoboPi.analogRead(0)
