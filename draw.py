import turtle
import numpy as np


def init(cell_size: int = 100, border: int = 100):
    scr = init_screen()
    pen = init_turtle()
    start_x, start_y = border, scr.window_height() - border
    pen.goto(start_x, start_y)
    return Draw(pen, cell_size)


def init_screen(scr_width: int = 1000, scr_height: int = 1000) -> turtle.TurtleScreen:
    # TODO implement aspect ratio support
    screen = turtle.Screen()
    screen.setup(scr_width + 4, scr_height + 8)  # w + 4, h + 8
    screen.setworldcoordinates(0, 0, scr_width, scr_height)
    return screen


def init_turtle(pen_size: int = 5) -> turtle.Turtle:
    trtl = turtle.Turtle()
    trtl.hideturtle()
    trtl.penup()
    trtl.pen(pensize=pen_size)

    return trtl


class Draw:
    def __init__(self, pen: turtle.Turtle, cell_size: int = 100):
        self.pen = pen
        self.cell_size = cell_size
        self.start_x, self.start_y = self.pen.position()

    # drawing
    def draw_cell(self, cell: np.ndarray):
        """
        :param cell: 1d array of len 4
        """

        actions = [self.right, self.down_left, self.up, self.down_right]

        for action, boolean in zip(actions, cell):
            if boolean:
                self.pen.pendown()
            else:
                self.pen.penup()

            action()
        self.pen.penup()

    # movement
    def right(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x + self.cell_size, pos_y)

    def left(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x - self.cell_size, pos_y)

    def up(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x, pos_y + self.cell_size)

    def down(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x, pos_y - self.cell_size)

    def down_right(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x + self.cell_size, pos_y - self.cell_size)

    def down_left(self):
        pos_x, pos_y = self.pen.position()
        self.pen.goto(pos_x - self.cell_size, pos_y - self.cell_size)

    # traversal
    def next_cell(self):
        """move up"""
        self.up()

    def next_row(self):
        """move to start x and down """
        self.down()
        self.pen.setx(self.start_x)

    # utility
    @staticmethod
    def done():
        turtle.done()
