import RoboPiLib as RPL
import time
import curses
import setup

t1 = 0.5
t2 = 1
t3 = 2
t4 = 4

def rotation():
  RPL.servoWrite(1,2000)
  time.sleep(t4)
  RPL.servoWrite(1,0)
  
key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - 360 degrees')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    rotation()
