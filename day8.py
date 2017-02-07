import numpy as np


class Grid(object):
    def __init__(self):
        self.grid = np.zeros([6, 50])

    def run(self, lines):
        for line in lines:
            self.parse_command(line)

    def parse_command(self, line):
        # Extract col or row or rect
        words = line.split()
        if words[0] == 'rect':
            coords = words[1].split('x')
            rows = int(coords[1])
            cols = int(coords[0])
            self.light_up(rows=rows, cols=cols)

        elif words[0] == 'rotate':
            col_or_row = words[1]
            by = int(words[-1])
            index = int(words[2].split('=')[1])
            self.rotate(col_or_row=col_or_row, index=index, by=by)

    def light_up(self, rows, cols):
        # set all in grid to 1
        self.grid[0:rows, 0:cols] = 1

    def rotate(self, col_or_row, index, by):
        # rotate col or row by n_steps
        if col_or_row == 'column':
            self.grid[:, index] = np.roll(self.grid[:, index], by)
        elif col_or_row == 'row':
            self.grid[index, :] = np.roll(self.grid[index, :], by)

    def print_code(self):
        chars = []
        for ii in range(0, 6):
            for jj in range(0, 50):
                if self.grid[ii, jj] == 1:
                    chars.append('#')
                else:
                    chars.append(' ')
            chars.append('\n')
        output = ''.join(chars)
        print output

grid = Grid()

with open('input_d8.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]

grid.run(lines)

print np.sum(grid.grid)
grid.print_code()
