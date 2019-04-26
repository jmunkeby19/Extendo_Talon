import RoboPiLib as RPL
import time
import curses
RPL._______

screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()

speed1 =      #Motor forwards
speed2 =      #Motor backwards
t1 =          #time.sleep
t2 =          #time.sleep

def lower():
  RPL._____(#, #)
  RPL._____(#, #)

def rise():
  RPL.
  RPL.

key = ''

while key != ord('q'):
  key = screen.getch()
  screen.clear()
  screen.addstr('q - quit | a - lower | s - rise')
  if key == ord('q'):
    curses.endwin()
  if key == ord('a'):
    lower()
  if key == ord('s'):
    rise()
