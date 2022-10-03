from __future__ import annotations

import numpy as np
import draw


class Grid:
    def __init__(self, width: int, height: int, p: float = 0.5):
        self.width = width
        self.height = height
        if 0 <= p <= 1:
            self.p = p
        else:
            raise ValueError(f'Argument p should be a float between 0 and 1')
        self.grid = self.init_grid()

    def init_grid(self):
        """
        Create the grid
        """
        DEPTH = 4

        return np.random.choice(a=[True, False],
                                size=(DEPTH, self.height, self.width),
                                p=[self.p, 1 - self.p])

    def __str__(self):
        return self.grid.__str__()

    def __repr__(self):
        return f'Grid(width={self.width}, height={self.height}, p={self.p})'


def main():
    grid = Grid(8, 8)

    drawer = draw.init()
    for row in range(grid.height):
        for col in range(grid.width):
            drawer.draw_cell(grid.grid[:, row, col])
            drawer.next_cell()
        drawer.next_row()
    drawer.done()


if __name__ == "__main__":
    main()
