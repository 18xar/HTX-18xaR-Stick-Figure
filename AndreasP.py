import arcade


def AndreasP(x, y):
    # BACKGROUND
    arcade.draw_rectangle_filled(x + 20, y + 50, 40, 60, arcade.color.AIR_FORCE_BLUE)
    arcade.draw_rectangle_filled(x + 20, y + 10, 40, 20, arcade.color.GREEN)
    # HEAD
    arcade.draw_circle_filled(x + 20, y + 60, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 17, y + 62, 1, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 23, y + 62, 1, arcade.color.WHITE)
    # BODY
    arcade.draw_line(x + 20, y + 60, x + 20, y + 36, arcade.color.BLACK, 2)
    arcade.draw_line(x + 20, y + 36, x + 16, y + 20, arcade.color.BLACK, 2)
    arcade.draw_line(x + 16, y + 20, x + 20, y + 6, arcade.color.BLACK, 2)
    arcade.draw_line(x + 20, y + 36, x + 34, y + 24, arcade.color.BLACK, 2)
    arcade.draw_line(x + 34, y + 24, x + 18, y + 20, arcade.color.BLACK, 2)
    arcade.draw_line(x + 20, y + 45, x + 34, y + 52, arcade.color.BLACK, 2)
    arcade.draw_line(x + 34, y + 52, x + 36, y + 64, arcade.color.BLACK, 2)
    arcade.draw_line(x + 20, y + 45, x + 6, y + 52, arcade.color.BLACK, 2)
    arcade.draw_line(x + 6, y + 52, x + 4, y + 64, arcade.color.BLACK, 2)



