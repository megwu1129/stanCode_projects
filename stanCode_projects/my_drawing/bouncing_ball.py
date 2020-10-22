"""
File: Bouncing ball
Name: Meg Wu
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 4
DELAY = 15
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
# create the first ball in the window
firstball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
firstball.filled = True
# record the count
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(firstball)
    onmouseclicked(event)


def event(mouse):
    """
    if the ball is at (START_X, START_Y) and the count < 3, move the ball
    """
    if firstball.x == START_X and count < 3:
        ballmove()
    else:
        return


def ballmove():
    """
    move the ball if the ball is in the window
    """
    global GRAVITY, firstball, count
    vy = 1
    # while firstball.x < window.width:
    #     firstball.move(VX, vy)
    #     pause(DELAY)
    #     vy += GRAVITY
    #     if firstball.y >= window.height:
    #         vy = -vy*REDUCE
    #
    # firstball = set_up_ball()
    # # add one in the count
    # count += 1
    # # when the while loop is over, create a new ball at (START_X, START_Y)
    # window.add(firstball)
    firstball.move(VX, vy)
    pause(DELAY)
    while firstball.x != START_X:
        firstball.move(VX, vy)
        pause(DELAY)
        vy += GRAVITY
        if firstball.y >= window.height:
            vy = -vy*REDUCE
        if firstball.x >= window.width:
            firstball = set_up_ball()
            count += 1
            window.add(firstball)



def set_up_ball():
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    return ball





if __name__ == "__main__":
    main()
