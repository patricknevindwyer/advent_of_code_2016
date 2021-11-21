#!/usr/bin/python3

import sys


def read_instructions(filename):
    with open(filename, "r") as file:
        return file.read().split("\n")

def load_commands(filename):
    """
    Load our commands. This returns a list of tuples to work from.
    
        [
            (rect, 3, 1),
            (rotate_row, 5, 2),
            (rotate_col, 1, 19)
        ]
    
    rect #x#
    rotate row y=# by #
    rotate column x=# by #
    """
    insts = []
    for raw in read_instructions(filename):
        if raw.startswith("rect "):
            (a, b) = raw.replace("rect ", "").split("x")
            insts.append( ("rect", int(a), int(b)) )
        elif raw.startswith("rotate row"):
            (a, b) = raw.replace("rotate row y=", "").split(" by ")
            insts.append( ("rotate_row", int(a), int(b)) )
        elif raw.startswith("rotate column"):
            (a, b) = raw.replace("rotate column x=", "").split(" by ")
            insts.append( ("rotate_col", int(a), int(b)) )
    
    return insts
    

class Grid(object):
    
    def __init__(self, width=50, height=6):
        self._grid = [self._empty_row(width) for r in range(height)]
        self._width = width
        self._height = height
    
    def _empty_row(self, width):
        return [0 for i in range(width)]
    
    def rect(self, width, height, state=1):
        """
        Turn all pixels on in the width, height area.
        """
        for row_idx in range(height):
            for col_idx in range(width):
                self._grid[row_idx][col_idx] = state
    
    def rotate_row(self, row, cycles):
        """
        Rotate the given row cycles number of positions
        """
        r = self._grid[row]
        rot_size = cycles % self._width
        n_r = r[self._width - rot_size:] + r[:self._width - rot_size]
        self._grid[row] = n_r
    
    def rotate_col(self, col, cycles):
        """
        Rotate the given column cycles number of positions
        """
        col_data = [self._grid[r][col] for r in range(self._height)]
        rot_size = cycles % self._height
        new_col_data = col_data[self._height - rot_size:] + col_data[:self._height - rot_size]
        for idx in range(self._height):
            self._grid[idx][col] = new_col_data[idx]
    
    def display(self):
        for row_idx in range(self._height):
            for col_idx in range(self._width):
                c = self._grid[row_idx][col_idx]
                if c == 1:
                    print("#", flush=False, end="")
                elif c == 0:
                    print(".", flush=False, end="")
            print("", flush=True)
    
    def count_in_state(self, state=1):
        c = 0
        for row_idx in range(self._height):
            for col_idx in range(self._width):
                if self._grid[row_idx][col_idx] == state:
                    c += 1
        return c
                

def run_interpreter(grid, insts):
    
    for (inst, a, b) in insts:
        if inst == "rect":
            grid.rect(a, b)
        if inst == "rotate_row":
            grid.rotate_row(a, b)
        if inst == "rotate_col":
            grid.rotate_col(a, b)


if __name__ == "__main__":
    grid = Grid()
    insts = load_commands(sys.argv[-1])
    
    print(grid.display())
    print("===")
    run_interpreter(grid, insts)
    print(grid.display())
    print("===")
    print("%d pixels lit" % (grid.count_in_state(),))
    
    