#!/bin/env python3
import requests
import curses

username='username'
password='password'

payload = {'usr': username, 'pwd': password}
url = 'http://192.168.178.175:88/cgi-bin/CGIProxy.fcgi'

def do_move(cmd):
    mypl = payload
    payload['cmd'] = cmd
    r = requests.get(url, params=mypl)

def run_loop():
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

    stdscr.addstr(0,10,"Hit 'q' to quit")
    stdscr.refresh()
    key = ''
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.addch(20,25,key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            stdscr.addstr(2, 20, "Up")
            do_move("ptzMoveUp")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(3, 20, "Down")
            do_move("ptzMoveDown")
        elif key == curses.KEY_LEFT:
            stdscr.addstr(3, 20, "Left")
            do_move("ptzMoveLeft")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(3, 20, "Right")
            do_move("ptzMoveRight")
        elif key == curses.KEY_END:
            stdscr.addstr(3, 20, "Stop")
            do_move("ptzStopRun")
    curses.endwin()

run_loop()
