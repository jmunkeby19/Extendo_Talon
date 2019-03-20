import Voss_RoboPiLib as RPL
import time
import curses
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

#2.0 inches/second times
#t1 = 5.0
#t2 = 2.5
#t3 = 0.5
#t4 = 0.125
#t5 = 0.35

#2.1 inches/second times
#t1 = 4.762
#t2 = 2.381
#t3 = 0.476
#t4 = 0.060
#t5 = 0.359

#2.2 inches/second times
t1 = 4.5454
t2 = 2.2727
t3 = 0.4545
t4 = 0.1136
t5 = 0.3425

#2.3 inches/second times
#t1 = 4.348
#t2 = 2.174
#t3 = 0.435
#t4 = 0.109
#t5 = 0.328

#Original times for 2.0584 inches/second
#t1 = 4.62325
#t2 = 0.462325
#t3 = 0.231625
#t4 = 0.115581
#t5 = 0.359

speed1 = 500
speed2 = 2000
speed3 = 0

def extend():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  
def retract():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed2, speed2 * 2)

def stop():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)

def extend_tenin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t1)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
        
def extend_fivein():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t2)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def extend_onein():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t3)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def extend_fourthin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t4)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def retract_extra():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed2, speed2 * 2)
  time.sleep(t5)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - extend | s - retract | d - stop | z - extend 10in | x - extend 1in | c - extend 0.5in | v - extend 0.25in | b - retract 0.7535in')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    extend()
  if key == ord('s'):
    retract()
  if key == ord('d'):
    stop()
  if key == ord('z'):
    extend_tenin()
  if key == ord('x'):
    extend_fivein()
  if key == ord('c'):
    extend_onein()
  if key == ord('v'):
    extend_fourthin()
  if key == ord('b'):
    retract_extra()
