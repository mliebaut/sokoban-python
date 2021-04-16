import curses
import MapReader
import Player

def main(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)

    mapReader = MapReader.MapReader('map')

    if mapReader.verifyMap() == False:
        curses.endwin()
        exit()

    player = Player.Player()
    

    mapReader.displayMap(stdscr)
    while True:
        
        entry = stdscr.getch()
        stdscr.clear()
        print(entry)
        
        if entry == 27 or entry == 113:
            curses.endwin()
            exit()
            
        if entry == curses.KEY_UP:
            player.moveUp(self)
            stdscr.refresh()
        
if __name__ == "__main__":
    curses.wrapper(main)