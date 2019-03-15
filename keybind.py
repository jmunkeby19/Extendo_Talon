import Voss_RoboPiLib as RPL
import time
import curses
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

t1 = (4.62325)
t2 = ()
t3 = ()
t4 = ()
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

def extend10():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t1)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
        
def extend1():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t2)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def extend_halfin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t3)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
def extend_quarterin():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t4)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - extend | s - retract | d - stop')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    extend()
  if key == ord('s'):
    retract()
  if key == ord('d'):
    stop()
  if key == ord('z'):
    extend10()
  if key == ord('x'):
    extend1()
