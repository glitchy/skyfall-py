import curses 
import time 
import sys
import random
import os

# gets the terminals screen size by lines and columns
os.get_terminal_size()

# clears the terminal screen
stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

quote = "THINK ON YOUR SINS".center(os.get_terminal_size().columns)
words = list(quote)

time.sleep(3)

# makes cursor invisible
curses.curs_set(False)

# moves cursor halfway down window
print(int((os.get_terminal_size().lines / 2) - 2) * '\n')

# iterates through every value in list
for letter in words:
    time.sleep(random.uniform(.03, .05))
    # prints on same line
    print(letter, end='')
    sys.stdout.flush()

time.sleep(3)

# screen refresh
stdscr.refresh()

# makes cursor invisible again
curses.curs_set(True)

# undo comments below for additional ending
# paragraph = "THINK ON YOUR SINS " * 150
# text = list(paragraph)
time.sleep(3)

# for letter in text:
#    time.sleep(.005)
#    # prints on same line
#    print(letter, end='')
#    sys.stdout.flush()


# properly ends program
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
