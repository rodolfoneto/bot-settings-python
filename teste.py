import curses

def display_list(stdscr, items):
    # Set up curses
    curses.curs_set(0)
    stdscr.nodelay(True)
    
    # Calculate the number of visible lines in the window
    rows, cols = stdscr.getmaxyx()
    num_visible_lines = rows - 1  # Leave one line for user input

    current_pos = 0
    while True:
        stdscr.clear()

        # Display the visible items
        for i in range(current_pos, min(current_pos + num_visible_lines, len(items))):
            stdscr.addstr(i - current_pos, 0, items[i])

        stdscr.refresh()

        # Get user input
        user_input = stdscr.getch()
        if user_input == ord('q'):  # Press 'q' to quit
            break
        elif user_input == curses.KEY_UP and current_pos > 0:
            current_pos -= 1
        elif user_input == curses.KEY_DOWN and current_pos < len(items) - 1:
            current_pos += 1

if __name__ == "__main__":
    items = [
        "Item 1",
        "Item 2",
        "Item 3",
        "Item 4",
        "Item 5",
        "Item 6",
        "Item 7",
        "Item 8",
        "Item 9",
        "Item 10",
        "Item 11",
        "Item 12",
        "Item 13",
        "Item 14",
        "Item 15",
    ]

    curses.wrapper(display_list, items)