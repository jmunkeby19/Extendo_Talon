import Voss_RoboPiLib as RPL
import time
import curses
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

t1 = (2)
t2 = (4.5084)
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

def extend2():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t1)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
        
def extend3():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed1, speed1 * 2)
  time.sleep(t2)
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, speed3, speed3 * 2)
  
key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('Hit q to quit, and a, s, or d to run extendo.')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    extend()
  if key == ord('s'):
    retract()
  if key == ord('d'):
    stop()
  if key == ord('f'):
    extend2()
  if key == ord('g'):
    extend3()
