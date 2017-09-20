import requests

username='username'
password='password'

payload = {'usr': username, 'pwd': password}
url = 'http://192.168.178.175:88/cgi-bin/CGIProxy.fcgi'
import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

def do_move(cmd):
    mypl = payload
    payload['cmd'] = cmd
    stdscr.addstr(4, 20, str(mypl))
    r = requests.get(url, params=mypl)
    stdscr.addstr(5, 20, str(r.url))

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
    elif key == curses.KEY_ENTER:
        stdscr.addstr(3, 20, "Stop")
        do_move("ptzStopRun")
curses.endwin()
