import RoboPiLib as RPL
import time
import curses
import setup

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

t1 = 4        #360
t2 = 2        #180
t3 = 1        #90
t4 = 0.5      #45
t5 = 0.166    #15
t6 = 0.111    #10
t7 = 0.055    #5

def clock_360():
  RPL.servoWrite(1,2000)
  time.sleep(t1)
  RPL.servoWrite(1,0)

def clock_180():
  RPL.servoWrite(1,2000)
  time.sleep(t2)
  RPL.servoWrite(1,0)

def clock_90():
  RPL.servoWrite(1,2000)
  time.sleep(t3)
  RPL.servoWrite(1,0)

def clock_45():
  RPL.servoWrite(1,2000)
  time.sleep(t4)
  RPL.servoWrite(1,0)

def clock_15():
  RPL.servoWrite(1,2000)
  time.sleep(t5)
  RPL.servoWrite(1,0)

def clock_10():
  RPL.servoWrite(1,2000)
  time.sleep(t6)
  RPL.servoWrite(1,0)

def clock_5():
  RPL.servoWrite(1,2000)
  time.sleep(t7)
  RPL.servoWrite(1,0)

def cclock_360():
  RPL.servoWrite(1,1000)
  time.sleep(t1)
  RPL.servoWrite(1,0)

def cclock_180():
  RPL.servoWrite(1,1000)
  time.sleep(t2)
  RPL.servoWrite(1,0)

def cclock_90():
  RPL.servoWrite(1,1000)
  time.sleep(t3)
  RPL.servoWrite(1,0)

def cclock_45():
  RPL.servoWrite(1,1000)
  time.sleep(t4)
  RPL.servoWrite(1,0)

def cclock_15():
  RPL.servoWrite(1,1000)
  time.sleep(t5)
  RPL.servoWrite(1,0)

def cclock_10():
  RPL.servoWrite(1,1000)
  time.sleep(t6)
  RPL.servoWrite(1,0)

def cclock_5():
  RPL.servoWrite(1,1000)
  time.sleep(t7)
  RPL.servoWrite(1,0)

key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - 360 | s - 180 | d - 90 | f - 45 | g - 15 | h - 10 | j - 5')
  screen.addstr('q - quit | z - 360 | x - 180 | c - 90 | v - 45 | b - 15 | n - 10 | m - 5')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    clock_360()
  if key == ord('s'):
    clock_180()
  if key == ord('d'):
    clock_90()
  if key == ord('f'):
    clock_45()
  if key == ord('g'):
    clock_15()
  if key == ord('h'):
    clock_10()
  if key == ord('j'):
    clock_5()

  if key == ord('z'):
    cclock_360()
  if key == ord('x'):
    cclock_180()
  if key == ord('c'):
    cclock_90()
  if key == ord('v'):
    cclock_45()
  if key == ord('b'):
    cclock_15()
  if key == ord('n'):
    cclock_10()
  if key == ord('m'):
    cclock_5()
