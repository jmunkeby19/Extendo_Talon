import Voss_RoboPiLib as RPL
import time
import curses
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

#inches/second final times
t1 = 4.5
t2 = 2.17
t3 = 0.335
t4 = 0.1
t5 = 0.04
t6 = 0.2

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

#2.15 inches/second times
#t1 = 4.651
#t2 = 2.326
#t3 = 0.35
#t4 = 0.116
#t5 = 0.2

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
  
def extend_halfin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t4)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def extend_quarterin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t5)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def retract_extra():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed2, speed2 * 2)
  time.sleep(t6)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - extend | s - retract | d - stop | z - extend 10in | x - extend 5in | c - extend 1in | v - extend 0.25in | b - retract 0.7535in')
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
    extend_halfin()
  if key == ord('b'):
    extend_quarterin()
  if key == ord('n'):
    retract_extra()
