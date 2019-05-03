import arcade


def AslakD(x, y):
    # flag
    arcade.draw_triangle_filled(x, y, x + 40, y + 80, x + 40, y + 0, (0, 0, 0))
    arcade.draw_triangle_filled(x, y, x + 40, y + 80, x + 0, y + 80, (255, 0, 0))
    # head
    arcade.draw_circle_outline(x + 25, y + 60, 10, (255, 255, 255))
    # body
    arcade.draw_line(x + 25, y + 50, x + 25, y + 22, (255, 255, 255))
    # left leg
    arcade.draw_line(x + 25, y + 22, x + 11, y + 6, (255, 255, 255))
    # right leg
    arcade.draw_line(x + 25, y + 22, x + 39, y + 6, (255, 255, 255))
    # arms
    arcade.draw_line(x + 11, y + 40, x + 39, y + 40, (255, 255, 255))
    # hammer
    arcade.draw_line(x + 15, y + 67, x + 5, y + 75, (255, 255, 0))
    arcade.draw_circle_filled(x + 5, y + 75, 2, (255, 255, 0))
    # sickle
    arcade.draw_line(x + 3, y + 66, x + 4, y + 68, (255, 255, 0))
    arcade.draw_arc_outline(x + 8, y + 73, 5, 5, (255, 255, 0), 0, 45)
    arcade.draw_arc_outline(x + 8, y + 73, 5, 5, (255, 255, 0), 225, 360)
    # face
    arcade.draw_text('uwu', x + 17, y + 56, (255, 255, 255), 7)