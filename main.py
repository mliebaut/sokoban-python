import curses
import MapReader

def main(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)

    mapReader = MapReader.MapReader('map')
    print(mapReader.verifyMap())


    while True:
        entry = stdscr.getch()
        print(entry)
        
        if entry == 27 or entry == 113:
            curses.endwin()
            exit()
        
if __name__ == "__main__":
    
    curses.wrapper(main)