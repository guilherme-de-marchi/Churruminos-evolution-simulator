import curses

class Window:
    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()

    def print(self, *args: str):
        self.window.clear()
        for arg in args:
            self.window.addstr(arg + '\n')

        self.window.refresh()