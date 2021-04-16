import curses

def main(stdscr):
    curses.noecho()
    curses.curs_set(0)
    stdscr.keypad(True)
    


    while True:
        entry = stdscr.getch()
        print(entry)
        
        if entry == 27:
            curses.endwin()
            exit()
        
if __name__ == "__main__":
    
    curses.wrapper(main)