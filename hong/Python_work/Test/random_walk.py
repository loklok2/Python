from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=100, rows=10, cols=10):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.rows = rows
        self.cols = cols 
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]

    def fill_walk(self, x_start=0, y_start=0):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        x = x_start
        y = y_start
        while len(self.x_values) < self.num_points:
            #x,y는 현재 좌표

            # Decide which direction to go, and how far to go.
            x_new = x + choice([1, 0, -1])
            y_new = choice([1, 0, -1])
            if x_new <= 0 or x_new >= self.rows or y_new <=0 or y_new >= self.cols:
                continue
            x, y= x_new, y_new
            self.board[x][y] += 1


        