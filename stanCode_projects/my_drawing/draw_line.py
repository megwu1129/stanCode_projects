"""
File: Draw a line
Name: Meg Wu
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
# set the count with 1
count = 1
# set the first click with location_x1 and location_y1
location_x1 = 0
location_y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    draw a line
    """
    global count, location_x1, location_y1
    hole = GOval(SIZE, SIZE)
    hole.filled = True
    hole.fill_color = 'white'
    window.add(hole, mouse.x-SIZE//2, mouse.y-SIZE//2)
    firstlocation = window.get_object_at(location_x1, location_y1) # record the first click as firstlocation
    if count == 1:
        location_x1 = mouse.x
        location_y1 = mouse.y
        count += 1
    #if the count is even, draw a line and remove the firstlocation
    elif count % 2 == 0:
        location_x2 = mouse.x
        location_y2 = mouse.y
        line = GLine(location_x1, location_y1, location_x2, location_y2)
        window.add(line)
        window.remove(hole)
        window.remove(firstlocation)
        count += 1
    # if the count is odd, record the location of the first click as location_x1 and location_y1
    elif count % 2 == 1 and count != 1:
        location_x1 = mouse.x
        location_y1 = mouse.y
        count += 1









if __name__ == "__main__":
    main()
