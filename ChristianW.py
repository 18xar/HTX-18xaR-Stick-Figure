import arcade


def ChristianW(x, y):
    # legs
    arcade.draw_rectangle_filled(x + 12, y + 14, 6, 28, (30, 30, 255))
    arcade.draw_rectangle_filled(x + 25, y + 14, 6, 28, (30, 30, 255))

    # body
    arcade.draw_rectangle_filled(x + 19, y + 36, 19, 36, (30, 30, 255))

    # arms
    arcade.draw_rectangle_filled(x + 6, y + 51, 6, 6, (30, 30, 255))
    arcade.draw_rectangle_filled(x + 31, y + 51, 6, 6, (30, 30, 255))

    # neck
    arcade.draw_rectangle_filled(x + 19, y + 57, 8, 6, (30, 30, 255))

    # head
    arcade.draw_rectangle_filled(x + 19, y + 66, 12, 16, (255, 255, 255))
