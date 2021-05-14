import curses

class Window:
    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()

    def print(self, target: list):
        self.window.clear()
        for row in target:
            self.window.addstr(''.join(row) + '\n')

        self.window.refresh()