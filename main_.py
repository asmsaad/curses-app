import curses

def main(stdscr):
    # Initialize curses
    curses.start_color()
    curses.curs_set(0)  # Hide the cursor

    # Define color codes
    RED = 1
    CLAY = 2



    # Clear screen
    stdscr.clear()

    for i in range(10):
        CLAY = i
        # Initialize colors

        curses.init_color(CLAY, 178, 102, 34)  # Define the clay color (RGB in range 0-1000)
        curses.init_pair(1, curses.COLOR_YELLOW, CLAY)
        # Use the color pair
        stdscr.attron(curses.init_pair(1, curses.COLOR_YELLOW, CLAY))
        stdscr.addstr(i, 0, f"This is red text on a clay background {str(CLAY)}", curses.color_pair(1))
        stdscr.attroff(curses.init_pair(1, curses.COLOR_YELLOW, CLAY))

    # Refresh to update the screen
    stdscr.refresh()

    # Wait for user input
    stdscr.getch()

# Run the main function inside curses wrapper
curses.wrapper(main)
